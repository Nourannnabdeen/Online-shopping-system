# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_sizes = models.CharField(max_length=100)  # Ensure this field exists
    image = models.ImageField(upload_to='products/')

    def _str_(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields you need, like total_price, etc.

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Allow null for user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} (x{self.quantity}) for {self.user.username}'
    @property
    def total_price(self):
        return self.quantity * self.product.price
    @property
    def total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

    def _str_(self):
        return f"Order {self.id} - {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.price