from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),  # API endpoint to fetch products
    path('cart/', views.cart_view, name='cart'),  # Cart view
    path('checkout/', views.checkout_view, name='checkout'),  # Checkout view
    path('login/', views.login_view, name='login'),  # Login view
    path('register/', views.register_view, name='register'),  # Register view
]