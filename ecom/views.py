from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from .models import Category, Product
from django.core.paginator import EmptyPage, InvalidPage, Paginator


# Create your views here.

def procat(request, c_slug=None):
    # Initialize variables
    c_page = None  # Current category page
    products_list = None  # List of products
    category = Category.objects.all()  # Get all categories

    if c_slug is not None:
        # If a category slug is provided in the URL
        c_page = get_object_or_404(Category, slug=c_slug)  # Retrieve the category based on the slug
        products_list = Product.objects.filter(category=c_page,
                                               available=True)  # Filter products by the selected category
    else:
        # If no category slug is provided, show all available products
        products_list = Product.objects.filter(available=True)

    # Pagination
    paginator = Paginator(products_list, 4)  # Create a paginator with 4 products per page
    try:
        pages = int(request.GET.get('page', '1'))  # Get the requested page number from the URL parameter
    except:
        pages = 1  # Default to the first page if the page number is not valid

    try:
        products = paginator.page(pages)  # Get the products for the specified page
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)  # Handle cases where the page is out of range

    # Render the 'category.html' template with category, products, and the list of categories
    return render(request, 'category.html', {'c_page': c_page, 'products': products, 'category': category})


def proDetail(request, c_slug, product_slug):
    try:
        # Get the product based on the category and product slug
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e  # Handle exceptions if the product is not found

    # Render the 'product.html' template with the product details
    return render(request, 'product.html', {'product': product})


def add(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        # slug = request.POST.get('slug', '')
        slug = slugify(name)
        desc = request.POST.get('desc', '')
        price = request.POST.get('price', '')
        category_name = request.POST.get('category', '')  # Get category name from the form

        # Retrieve the Category instance based on the name
        category = Category.objects.get(name=category_name)

        img = request.FILES.get('img', '')
        stock = request.POST.get('stock', '')

        # Check if 'available' checkbox is checked and handle its value accordingly
        available = request.POST.get('available') == 'on'

        product = Product(
            name=name, slug=slug, desc=desc, price=price, category=category, img=img, stock=stock, available=available)
        product.save()
        return redirect('ecom:ProCat')
    return render(request, 'add.html', {'categories': categories})
