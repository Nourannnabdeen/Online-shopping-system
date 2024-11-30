from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, CartItem, Cart
from .serializers import ProductSerializer, CartItemSerializer

# Product List API View
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# Cart View (ensure the user is logged in)
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not authenticated
    
    # Get the user's cart or create a new one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate total price for all items in the cart
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'shopping-cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Checkout View (ensure the user is logged in)
def checkout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not authenticated

    # Get the user's cart or create a new one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('cart')  # Redirect to the cart page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after registration
            return redirect('cart')  # Redirect to cart page after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})