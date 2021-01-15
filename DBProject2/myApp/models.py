from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length =30)
    edisg = models.CharField(max_length = 40)
    edob = models.CharField(max_length =30)
    eexp = models.FloatField()
    esal = models.IntegerField()
    def __str__(self):
        return str(self.eid)
