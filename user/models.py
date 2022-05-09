from django.contrib.auth.models import User
from django.db import models



# user_profile table name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9999, blank=True)
    date_of_birth = models.CharField(max_length=255, blank=True)
    profile_picture = models.CharField(max_length=9999, blank=True)
    bio = models.CharField(max_length=9999, blank=True)

    def __str__(self):
        return self.user



# class FireSaleCategory(models.Model):
# name = models.CharField(max_length=255)

# class FireSale(models.Model):
# name = models.CharField(max_length=255)
# description = models.CharField(max_length=255, blank=True)
# category = models.ForeignKey(FireSaleCategory, on_delete=models.CASCADE)
# price = models.FloatField()
# on_sale = models.BooleanField()
# user = models.ForeignKey(User, on_delete=models.CASCADE)