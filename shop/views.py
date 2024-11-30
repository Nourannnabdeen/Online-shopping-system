from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer
from django.contrib.auth.models import User  # Default User model

# Product List View
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()  # Get all products
        serializer = ProductSerializer(products, many=True)  # Serialize the products
        return Response(serializer.data)  # Return serialized data as JSON

# Cart View
class CartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')  # Get product ID from request
        user_id = request.data.get('user_id')  # Get user ID from request
        try:
            product = Product.objects.get(id=product_id)  # Fetch the product
            # Simulating adding product to a cart (can be improved with cart model/session)
            return Response({"message": f"Product '{product.name}' added to cart!"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found!"}, status=status.HTTP_404_NOT_FOUND)

# Checkout View
class CheckoutView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')  # Get user ID from request
        products = request.data.get('products')  # Get list of product IDs from request
        try:
            user = User.objects.get(id=user_id)  # Fetch the user
            order = Order.objects.create(user=user, total_price=0)  # Create an order
            total_price = 0

            for product_id in products:
                product = Product.objects.get(id=product_id)  # Fetch each product
                OrderItem.objects.create(order=order, product=product, quantity=1)  # Add order items
                total_price += product.price  # Calculate total price

            order.total_price = total_price  # Update total price
            order.save()  # Save the order

            return Response({"message": "Order placed successfully!"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({"error": "One or more products not found!"}, status=status.HTTP_404_NOT_FOUND)