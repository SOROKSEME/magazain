from django.db import models
from accounts.models import CustomUser
from pages.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=150)
    shipping = models.BooleanField(default=False)

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        return sum([product.quantity for product in order_products])

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        return sum([product.get_total_preci for product in order_products])


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.product * self.quantity


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    company_name = models.CharField(max_length=150)


class ShippingAddress(models.Model):
    country = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    comment = models.TextField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
