from django.contrib.auth.models import User
from django.db import models


class Shipping(models.Model):
    method = models.CharField(max_length=9999, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    street_name = models.CharField(max_length=9999, blank=True)
    house_number = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=9999, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=9999, blank=True)


class Payment(models.Model):
    cardholder_name = models.CharField(max_length=9999, blank=True)
    cardnumber = models.CharField(max_length=255, blank=True)
    expiration_date = models.CharField(max_length=9999, blank=True)
    cvc = models.CharField(max_length=9999, blank=True)
    payment_date = models.CharField(max_length=9999, blank=True)
    total_amoun = models.CharField(max_length=9999, blank=True)



