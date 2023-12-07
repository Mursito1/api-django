from django.db import models

# Create your models here.

class Profesor(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

class Alumno(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
