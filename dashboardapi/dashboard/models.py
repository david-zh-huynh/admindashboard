from django.db import models
from datetime import datetime
# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=60)
    units_sold = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=0)
    expire_date = models.DateTimeField(default=datetime.now)
