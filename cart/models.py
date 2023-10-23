from django.db import models
from django.contrib.auth import get_user_model
from packages.models import Package

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.package.title} in {self.user}'s cart"

    def total_price(self):
        return self.package.price * self.quantity


