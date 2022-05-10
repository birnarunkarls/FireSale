from django.contrib.auth.models import User
from django.db import models



# user_profile table name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=9999, default="")
    last_name = models.CharField(max_length=9999, default="")
    phone_number = models.CharField(max_length=9999, default="")
    date_of_birth = models.CharField(max_length=255, default="")
    profile_picture = models.CharField(max_length=9999, default="")
    bio = models.CharField(max_length=9999, default="")

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