from django.urls import path
from .views.views import product
from .views.cart_views import *

urlpatterns = [
    path('product/', product, name="product"),
    path('cart/', getCart, name="cart")
]