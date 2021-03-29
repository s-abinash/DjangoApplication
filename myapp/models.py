from django.db import models


class formcontact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    no = models.CharField(max_length=20)


# Create your models here.
