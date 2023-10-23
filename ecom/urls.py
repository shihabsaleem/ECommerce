from . import views
from django.urls import path

app_name = 'ecom'
urlpatterns = [
    path('', views.ProCat, name='ProCat'),
    path('<slug:c_slug>/',views.ProCat, name='ProByCat')
]
