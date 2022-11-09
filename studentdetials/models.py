from django.db import models

# Create your models here


class studentdb(models.Model):
    fullname = models.CharField(max_length=100)
    blood = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
