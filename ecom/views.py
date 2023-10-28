from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import EmptyPage, InvalidPage, Paginator


# Define a view for listing products by category
def procat(request, c_slug=None):
    c_page = None  # Initialize a variable to hold the category page
    products_list = None  # Initialize a variable to hold the list of products

    # Check if a category slug is provided
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)  # Get the category object based on the slug
        products_list = Product.objects.filter(category=c_page, available=True)  # Filter products by category
    else:
        products_list = Product.objects.filter(
            available=True)  # If no category slug is provided, filter all available products

    # Pagination
    paginator = Paginator(products_list, 4)  # Create a paginator with 4 products per page
    try:
        page = int(request.GET.get('page', '1'))  # Get the page number from the request's GET parameters
    except:
        page = 1  # Default to the first page if the page number is not valid

    try:
        products = paginator.page(page)  # Get the products for the specified page
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)  # Handle cases where the page is out of range

    # Render the 'category.html' template with the category and product data
    return render(request, 'category.html', {'c_page': c_page, 'products': products})


# Define a view for displaying product details
def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,
                                      slug=product_slug)  # Get the product based on category and product slugs
    except Product.DoesNotExist as e:
        raise e  # Handle the case where the product does not exist

    # Render the 'product.html' template with the product data
    return render(request, 'product.html', {'product': product})
