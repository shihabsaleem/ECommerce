from django.db import models  # Import the necessary modules from Django
from django.urls import reverse  # Import the reverse function to generate URLs

# Define the Category model
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)  # A character field for the category name
    slug = models.SlugField(max_length=250, unique=True)  # A slug field for the category URL
    desc = models.TextField(blank=True)  # A text field for category description (optional)
    img = models.ImageField(upload_to='category', blank=True)  # An image field for category image (optional)

    class Meta:
        ordering = ('name',)  # Define the default ordering of categories
        verbose_name = 'category'  # Singular name for the admin interface
        verbose_name_plural = 'categories'  # Plural name for the admin interface

    def get_url(self):
        # Define a method to generate the URL for a category
        return reverse('ecom:ProByCat', args=[self.slug])

    def __str__(self):
        # Define a string representation for the category object
        return '{}'.format(self.name)

# Define the Product model
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)  # A character field for the product name
    slug = models.SlugField(max_length=250, unique=True)  # A slug field for the product URL
    desc = models.TextField(blank=True)  # A text field for product description (optional)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # A decimal field for product price
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # A foreign key to Category with CASCADE delete behavior
    img = models.ImageField(upload_to='product', blank=True)  # An image field for product image (optional)
    stock = models.IntegerField()  # An integer field for product stock
    available = models.BooleanField(default=True)  # A boolean field indicating product availability
    created = models.DateTimeField(auto_now_add=True)  # A timestamp for product creation
    updated = models.DateTimeField(auto_now=True)  # A timestamp for product updates

    def get_url(self):
        # Define a method to generate the URL for a product
        return reverse('ecom:ProCatDetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)  # Define the default ordering of products
        verbose_name = 'product'  # Singular name for the admin interface
        verbose_name_plural = 'products'  # Plural name for the admin interface

    def __str__(self):
        # Define a string representation for the product object
        return '{}'.format(self.name)
