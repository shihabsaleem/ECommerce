# Import necessary modules
from django.contrib import admin
from .models import Category, Product  # Import Category and Product models from your application's models

# Define the admin interface for the Category model
class CategoryAdmin(admin.ModelAdmin):
    # Display 'name' and 'slug' fields in the admin list view
    list_display = ['name', 'slug']

    # Automatically populate the 'slug' field based on the 'name' field
    prepopulated_fields = {'slug': ('name',)}

# Register the Category model with the CategoryAdmin interface
admin.site.register(Category, CategoryAdmin)

# Define the admin interface for the Product model
class ProductAdmin(admin.ModelAdmin):
    # Display various fields in the admin list view
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']

    # Allow editing 'price', 'stock', and 'available' fields directly in the list view
    list_editable = ['price', 'stock', 'available']

    # Automatically populate the 'slug' field based on the 'name' field
    prepopulated_fields = {'slug': ('name',)}

    # Set the number of items displayed per page in the admin list view
    list_per_page = 20

# Register the Product model with the ProductAdmin interface
admin.site.register(Product, ProductAdmin)
