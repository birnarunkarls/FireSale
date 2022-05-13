from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from item.models import Item



class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default="")
    full_name = models.CharField(max_length=255, default="")
    street_name = models.CharField(max_length=9999, default="")
    house_number = models.CharField(max_length=255, default="")
    postal_code = models.CharField(max_length=9999, default="")
    city = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=9999, default="")
    cardholder_name = models.CharField(max_length=9999, default="")
    cardnumber = models.CharField(max_length=255, default="")
    expiration_date = models.CharField(max_length=9999, default="")
    cvc = models.CharField(max_length=9999, default="")



#class Payment(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
#    cardholder_name = models.CharField(max_length=9999, default="")
#    cardnumber = models.CharField(max_length=255, default="")
#    expiration_date = models.CharField(max_length=9999, default="")
#    cvc = models.CharField(max_length=9999, default="")
#    payment_date = models.CharField(max_length=9999, default="")
#    total_amount = models.FloatField(default=0)

#    def __str__(self):
#        return self.cardholder_name


#class Shipping(models.Model):
#    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, default="")
#    method = models.CharField(max_length=9999, default="")
#   full_name = models.CharField(max_length=255, default="")
#    street_name = models.CharField(max_length=9999, default="")
#    house_number = models.CharField(max_length=255, default="")
#    postal_code = models.CharField(max_length=9999, default="")
#    city = models.CharField(max_length=255, default="")
#    country = models.CharField(max_length=9999, default="")

#    def __str__(self):
#        return self.full_name


class Rating(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=None,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ])