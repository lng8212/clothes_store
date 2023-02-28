from django.urls import path
from .views.views import product
from .views.cart_views import *
from .views.order_views import *

urlpatterns = [
    path('product/', product, name="product"),
    path('cart/', getCart, name="cart"),
    path('cart/add', addToCart, name="add_to_cart"),
    path('order/create', createOrder, name="create_order"),
    path('order/', getOrder, name="get_order"),
]