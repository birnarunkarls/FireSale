from django.contrib.auth.models import User
from django.db import models
# from user.models import User

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=9999, default="")
    description = models.CharField(max_length=255, default="")
    condition = models.CharField(max_length=9999, default="")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    #highest_bid = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Bid(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    notification = models.CharField(max_length=255, default="")


class Images(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, default="")


