from django.urls import path
from . import views  # Import views from the current app

app_name = 'cart'  # Set the application namespace

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),  # URL pattern for adding a product to the cart
    path('', views.cart_detail, name='cart_detail'),  # URL pattern for viewing the cart
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('fremove/<int:product_id>/', views.full_remove, name='full_remove')
]
