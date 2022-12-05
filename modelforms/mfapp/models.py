from django.db import models

# Create your models here.


class mfforms(models.Model):
    name = models.CharField(max_length=40)
    Email = models.EmailField(max_length=30, default="ram@gmail.com")
    Address = models.TextField(max_length=300, default="fsadfasdfasdfasfasf")
