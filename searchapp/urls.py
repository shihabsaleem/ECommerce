from django.urls import path  # Import the path function for URL routing
from . import views  # Import views from the same application

app_name = 'searchapp'  # Define the application namespace

urlpatterns = [
    path('', views.searchResult, name='searchResult'),  # Define a URL pattern for the 'searchResult' view
]
