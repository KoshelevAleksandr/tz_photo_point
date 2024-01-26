from django.db import models


class Rate(models.Model):
    currency_rate = models.FloatField()
    pub_date = models.DateTimeField(auto_now_add=True)
