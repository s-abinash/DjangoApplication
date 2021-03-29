from django.db import models


class FormContact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    no = models.CharField(max_length=20)


class BioForm(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    age = models.IntegerField()

# Create your models here.
