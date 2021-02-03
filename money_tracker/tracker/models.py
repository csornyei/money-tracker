from django.db import models
from django.utils import timezone

class Spending(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now())