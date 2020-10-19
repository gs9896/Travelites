from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Destination(models.Model):
    place = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer = models.BooleanField(default=False)

class Complaints(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    complaint = models.TextField()

class Guides(models.Model):
    name = models.CharField(max_length=100)
    mailid = models.EmailField(max_length=300)
    place = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    img = models.ImageField(upload_to='pics')
    review = models.IntegerField()
    availability = models.BooleanField(default=False)