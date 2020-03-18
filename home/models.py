from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''class ParkingCards:
    place : str
    arrival_time : str
    departure_time : str
    date : str
    price : int'''
class ParkingCards(models.Model):
    place = models.TextField()
    arrival_time : models.TextField()
    departure_time : models.TextField()
    date : models.TextField()
    price : models.IntegerField()
