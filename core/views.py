from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import UserProfile, Category, Product, Order
from .serializers import (
    UserSerializer, UserProfileSerializer,
    CategorySerializer, ProductSerializer, OrderSerializer
)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"Жаңы колдонуучу түзүлдү: {user.username}"
            }
        )

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def ws_test(request):
    return render(request, 'ws_test.html')
