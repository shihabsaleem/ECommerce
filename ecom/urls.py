from . import views
from django.urls import path

app_name = 'ecom'
urlpatterns = [
    path('', views.procat, name='ProCat'),
    path('<slug:c_slug>/', views.procat, name='ProByCat'),
]
