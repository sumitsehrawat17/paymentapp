from django.db import models

# Create your models here.

from Recoperator.models import *
class recharge(models.Model):
    operat = models.ForeignKey(toperator,on_delete=models.CASCADE)
    phoneno = models.BigIntegerField()
    circle = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    

