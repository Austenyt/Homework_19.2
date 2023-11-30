from django.shortcuts import render

from main.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Магазин - Главная'
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Магазин - Контакты'
    }
    return render(request, 'main/contacts.html', context)


def category_products(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Магазин - Каталог товаров {category_item.name}'
    }
    return render(request, 'main/product.html', context)
