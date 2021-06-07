from django.db import models
from login.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, default="Select a Category")

    def __str__(self):
        return self.name

class Product(models.Model):
    item = models.CharField(max_length=255, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="productcategory", on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

class Order(models.Model):
    customer = models.ForeignKey(User, related_name="productcustomer", on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    items = models.IntegerField(default=0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name="productitem", on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, related_name="productorder", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    subtotal = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Shipping(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address     

