from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ParkingCards(models.Model):
    place = models.TextField()
    arrival_time : models.TextField()
    departure_time : models.TextField()
    date : models.TextField()
    price : models.IntegerField()

class Slots(models.Model):
    slot_number : models.TextField()
    color : models.TextField()
