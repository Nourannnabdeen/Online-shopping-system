from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Product Catalog
    path('products/', views.product_list_view, name='product-list'),


    # Shopping Cart
    path('cart/', views.cart_view, name='cart'),

    # Checkout
    path('checkout/', views.checkout_view, name='checkout'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]