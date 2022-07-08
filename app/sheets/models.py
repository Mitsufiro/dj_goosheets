from django.db import models


class Currency(models.Model):
    num_of_row = models.IntegerField()
    id_of_items = models.IntegerField()
    price = models.IntegerField()
    delivery_time = models.CharField(max_length=20)
    price_rub = models.FloatField()