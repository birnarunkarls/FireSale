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

    def __str__(self):
        return self.name




class Bid(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=9999, default="pending")


#class AcceptedBids(models.Model):
#    bid = models.ForeignKey(Bid, on_delete=models.CASCADE())
#    status = models.CharField(max_length=9999, default="pending")


class Images(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, default="")


