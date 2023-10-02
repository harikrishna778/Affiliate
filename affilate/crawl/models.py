from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=155, blank=True, null=True)
    price = models.CharField(max_length=40, blank=True, null=True)
    mrp = models.CharField(max_length=40, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    item_link = models.URLField(max_length=1000, null=True, blank=True)
    image_link = models.URLField(max_length=1000, null=True, blank=True)

    class Meta:
        unique_together = ['name', 'price', 'mrp', 'discount', 'item_link']
