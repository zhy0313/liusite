from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShoppingCart(models.Model):
    whoscart = models.OneToOneField(User)

    def __str__(self):
        return "购物车"
