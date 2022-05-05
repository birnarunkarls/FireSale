from django.db import models

# Create your models here.
class FireSaleCategory(models.Model):
    name = models.CharField(max_length=255)

class FireSale(models.model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(FireSaleCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class