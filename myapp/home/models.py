from django.db import models
from django.utils import timezone
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=20)

class Signup(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Auth(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    number = models.IntegerField()

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')