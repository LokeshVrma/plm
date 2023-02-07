from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    sales_price = models.FloatField(max_length=200)
    purchase_price = models.FloatField(max_length=200, null=True, blank=True, default=0)

    def __str__(self):
        return self.item_name
    
