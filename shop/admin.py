from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]   # fixed
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["title","category","price","stock","is_active","created_at",]

    list_filter = ["is_active","category","created_at","updated_at",]

    list_editable = ["price","stock","is_active",]

    search_fields = ["title","description",]

    prepopulated_fields = {"slug": ("title",)}

    autocomplete_fields = ["category"]

    ordering = ["-created_at"]