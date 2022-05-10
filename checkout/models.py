from django.contrib.auth.models import User
from django.db import models


class Shipping(models.Model):
    method = models.CharField(max_length=9999, default="")
    full_name = models.CharField(max_length=255, default="")
    street_name = models.CharField(max_length=9999, default="")
    house_number = models.CharField(max_length=255, default="")
    postal_code = models.CharField(max_length=9999, default="")
    city = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.full_name


class Payment(models.Model):
    cardholder_name = models.CharField(max_length=9999, default="")
    cardnumber = models.CharField(max_length=255, default="")
    expiration_date = models.CharField(max_length=9999, default="")
    cvc = models.CharField(max_length=9999, default="")
    payment_date = models.CharField(max_length=9999, default="")
    total_amount = models.FloatField(default="")

    def __str__(self):
        return self.cardholder_name



