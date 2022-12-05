from django.db import models

# Create your models here.


class mfforms(models.Model):
    name = models.CharField(max_length=23)
    catagory = models.CharField(max_length=500)
    village = models.CharField(max_length=50)
