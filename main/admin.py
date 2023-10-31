from django.contrib import admin

from main.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Выбранные поля для отображения в списке


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'purchase_price', 'category')  # Выбранные поля для отображения в списке
    list_filter = ('category',)  # Настройка фильтра по категории
    search_fields = ('title', 'description',)  # Настройка поиска по названию и описанию
