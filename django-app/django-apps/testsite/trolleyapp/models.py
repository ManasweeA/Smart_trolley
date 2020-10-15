from django.db import models

# Create your models here.

class inv(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    

class bill(models.Model):
    pid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    num = models.CharField(max_length=100, default="num")