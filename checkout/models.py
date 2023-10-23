from django.db import models
from django.contrib.auth import get_user_model
from packages.model import Package
from cart.models import CartItem
from django.conf import settings
from django.countries.fields import CountryField

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(get_user_models(), on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.OneToOneField(
        ShippingAddress, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True
    )
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.user} - {self.created_at}"

class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addressline_1 = models.CharField(max_length=50)
    addressline_2 = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    country = CountryField()

    def __str__(self):
        return f"Shipping Address for {self.user.username}"