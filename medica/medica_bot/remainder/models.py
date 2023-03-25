from django.db import models

class remainder(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField( max_length=1024) #color shape or liq of tablet
    number_time =models.IntegerField()
    time_gap = models.CharField( max_length=16)
    

# Create your models here.
