from django.contrib import admin

# Register your models here.
from orderflow.apps.catalog.models import Product,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =("name","created_at")
    search_fields = ("name",)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "is_active", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("name",)
