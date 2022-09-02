from django.shortcuts import render, redirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


def home1(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    data = {}
    data['categories'] = categories

    return render(request,'home.html',data)