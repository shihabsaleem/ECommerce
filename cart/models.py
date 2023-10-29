from django.db import models
from ecom.models import Product  # Import the Product model from the 'ecom' app


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)  # A unique identifier for the cart
    date_added = models.DateField(auto_now_add=True)  # Date when the cart was created

    class Meta:
        db_table = 'cart'  # Set the database table name to 'cart'
        ordering = ['date_added']  # Define the default ordering based on the date_added field

    def __str__(self):
        return self.cart_id  # Return a string representation of the cart (its ID)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # A link to the product being added to the cart
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # A link to the cart to which the product is added
    quantity = models.IntegerField()  # The quantity of the product in the cart
    active = models.BooleanField(default=True)  # Indicates whether the cart item is active

    class Meta:
        db_table = 'CartItem'  # Set the database table name to 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity  # Calculate the subtotal for the cart item

    def __str__(self):
        return str(self.product)  # Return a string representation of the cart item (the product's name)
