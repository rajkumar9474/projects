from django.db import models

# Create your models here.
class donate_blood(models.Model):
    name = models.CharField(max_length=15)
    ph_num = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    blood_group = models.CharField(max_length=3)
    health_disease = models.CharField(max_length=3)
    disease = models.CharField(max_length=20,default="")

