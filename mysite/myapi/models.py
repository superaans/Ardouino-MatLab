from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime, timedelta

# Getting Datetime from timestamp

class Dht11(models.Model):
    id = models.AutoField(primary_key = True)
    temp = models.FloatField(null=False)
    hum = models.FloatField(null=False)
    dt = models.DateTimeField(null=False)
