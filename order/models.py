from product.models import Product
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product , on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    def __str__(self):
        return self.product.title
