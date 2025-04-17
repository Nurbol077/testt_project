from django.contrib import admin
from .models import UserProfile, Category, Product, Order

# Admin панелине чагылдыруу үчүн класстарды түзүү
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)  # Бул жерде 'bio' жана 'date_of_birth' - сиздин моделде болуучу талаалар
    search_fields = ['user__username', 'bio']  # Пайдалануучунун атын жана био маалыматтарын издөө үчүн

# Каттоо
admin.site.register(UserProfile, UserProfileAdmin)  # UserProfile моделин админ панелинде көрсөтүү
admin.site.register(Category)  # Категория моделин каттоо
admin.site.register(Product)  # Продукт моделин каттоо
admin.site.register(Order)  # Заказ моделин каттоо