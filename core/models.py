from django.db import models

# Create your models here.

class client(models.Model):
    name = models.CharField(max_length=24)
    latitude = models.CharField(max_length=24)
    longtude = models.CharField(max_length=24)
    