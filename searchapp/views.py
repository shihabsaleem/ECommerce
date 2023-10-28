from django.shortcuts import render  # Import the render function to render templates
from django.db.models import Q  # Import the Q object for complex queries
from ecom.models import Product, Category  # Import the Product and Category models from the ecom app

# Create your views here.
def searchResult(request):
    products = None  # Initialize a variable to hold the search results
    query = None  # Initialize a variable to hold the search query

    if 'q' in request.GET:  # Check if the 'q' parameter is present in the request's GET parameters
        query = request.GET.get('q')  # Get the value of the 'q' parameter (the user's query)

        # Use the Q object to perform a search query on Product models based on name or description
        products = Product.objects.filter(Q(name__contains=query) | Q(desc__contains=query))

        # Render the 'search.html' template with the search query and search results
        return render(request, 'search.html', {'query': query, 'products': products})
