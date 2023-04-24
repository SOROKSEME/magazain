from django.contrib import admin
from .models import Category, Brand


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pk")
    list_display_links = ("title", "pk")
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
