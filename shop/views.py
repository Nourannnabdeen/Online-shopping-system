from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer


# Product List API View
def product_list_view(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'product-management.html', {'products': products})
    
def home(request):
    return render(request, 'index.html')

# Cart View
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create the cart
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate total price for all items in the cart
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'shopping-cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Checkout View
@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product-list')  # Redirect to product list after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-list')  # Redirect to product list after registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout