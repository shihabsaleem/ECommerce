# Import Category and Product models from your application's models
from .models import Category, Product

# Define a function named menu_links that takes a 'request' argument
def menu_links(request):
    # Retrieve all Category objects from the database
    links = Category.objects.all()

    # Return a dictionary containing the 'links' variable, which holds the Category objects
    return {'links': links}
