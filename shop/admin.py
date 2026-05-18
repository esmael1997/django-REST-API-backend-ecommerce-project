from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["title", "description",]
    prepopulated_fields = {"slug": ("name",)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "stock", "available", "created_at",]
    list_filter = ["available", "category", "created_at","updated_at",]
    list_editable = ["price", "stock", "available",]
    search_fields = ["title", "description",]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["category",]
    ordering = ["-created_at"]
