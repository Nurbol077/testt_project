from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, CategoryViewSet, ProductViewSet, OrderViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

# Роутерди түзүү
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

# API схемасын түзүү
schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL'дерди бириктирүү
urlpatterns = [
    path('', include(router.urls)),  # API роутерлерин кошуу
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ws_test/', views.ws_test, name='ws_test'),
]
