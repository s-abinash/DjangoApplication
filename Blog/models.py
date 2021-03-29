from django.db import models


# Create your models here.

class BlogPortal(models.Model):
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    content = models.CharField(max_length=3000)
    author = models.CharField(max_length=50)
