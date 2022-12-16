from django.db import models

# Create your models here.
class toperator(models.Model):
    op = models.CharField(max_length= 100, primary_key=True)

    def __str__(self):
        return self.op

class rechargeplans(models.Model):
    op = models.ForeignKey(toperator,on_delete=models.CASCADE)
    plan = models.BigIntegerField()
    description = models.TextField(default="")

    def __str__(self):
        return self.op.op
