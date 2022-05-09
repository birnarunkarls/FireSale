from django.contrib.auth.models import User
from django.db import models
from user.models import User


class Item(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=9999, default="")
    description = models.CharField(max_length=255, default="")
    condition = models.CharField(max_length=9999, default="")
    category = models.CharField(max_length=9999, default="")
    image = models.CharField(max_length=9999, default="IMG")
    highest_bid = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.name


class Bid(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=9999, blank=True)
    notification = models.CharField(max_length=255, blank=True)
