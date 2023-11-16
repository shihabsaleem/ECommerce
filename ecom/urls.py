from . import views  # Import views from the same directory
from django.urls import path  # Import the path function for URL routing

app_name = 'ecom'  # Define the application namespace

urlpatterns = [
    path('', views.procat, name='ProCat'),  # Define a URL pattern for the root (homepage)
    path('cat/<slug:c_slug>/', views.procat, name='ProByCat'),  # Define a URL pattern for category pages
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='ProCatDetail'),# Define a URL pattern for product detail pages
    path('add/', views.add, name='add'),
]
