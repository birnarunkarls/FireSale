from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from item.models import Item


class Countries(models.Model):
    country = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.country


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default="")
    full_name = models.CharField(max_length=255, default="")
    street_name = models.CharField(max_length=9999, default="")
    house_number = models.CharField(max_length=255, default="")
    postal_code = models.CharField(max_length=9999, default="")
    city = models.CharField(max_length=255, default="")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, default="")
    cardholder_name = models.CharField(max_length=9999, default="")
    cardnumber = models.CharField(max_length=255, default="")
    expiration_date = models.CharField(max_length=9999, default="")
    cvc = models.CharField(max_length=9999, default="")


    def __str__(self):
        return self.country


class Rating(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    rating = models.IntegerField(
        default=None,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ])