from django.shortcuts import render
from ecom.models import Product, Category
from django.db.models import Q


# Create your views here.
def searchResult(request):
    products = None
    query = None
    if 'q' is request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | (Q(desc__contains=query)))
        return render(request, 'search.html', {'query': query, 'products': products})
