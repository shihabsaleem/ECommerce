from django.shortcuts import render
from .models import Category, Product


# Create your views here.

def ProCat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'category.html', {'c_page': c_page, 'products': products})