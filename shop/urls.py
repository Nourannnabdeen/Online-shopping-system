from django.urls import path
from .views import ProductList, CartView, CheckoutView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),  # Product API
    path('cart/', CartView.as_view(), name='cart'),  # Cart API
    path('checkout/', CheckoutView.as_view(), name='checkout'),  # Checkout API
]