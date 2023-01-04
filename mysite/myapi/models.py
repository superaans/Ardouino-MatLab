from django.db import models

# Create your models here.
from django.db import models


class Dht11(models.Model):
    id = models.AutoField(primary_key = True)
    temp = models.FloatField(null=False)
    hum = models.FloatField(null=Flase)
    dt = models.DateTimeField(auto_now_add=True,null=True)
