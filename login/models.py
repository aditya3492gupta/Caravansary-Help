from django.db import models

# Create your models here.
class Food_request(models.Model):
    name=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    date=models.DateField()
    time=models.CharField(max_length=20)
    reason=models.TextField()

class Services(models.Model): 
    name=models.CharField(max_length=50)
    email=models.EmailField()
    room=models.CharField(max_length=50)
    message=models.TextField()
class Leave(models.Model):
    name=models.CharField(max_length=50)
    admn=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    reason=models.CharField(max_length=50)
    relate=models.CharField(max_length=50)
    rphone=models.CharField(max_length=50)
    add=models.CharField(max_length=50)
    info=models.CharField(max_length=50)
    rdate=models.CharField(max_length=50)
    rtime=models.CharField(max_length=50)
class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
class Laundry(models.Model):
    name=models.CharField(max_length=40)
    admn=models.CharField(max_length=15)
    inputp=models.CharField(max_length=2)
    inputj=models.CharField(max_length=2)
    inputs=models.CharField(max_length=2)
    inputt=models.CharField(max_length=2)
    inputk=models.CharField(max_length=2)
    inputpy=models.CharField(max_length=2)
    inputtp=models.CharField(max_length=2)
    inputsho=models.CharField(max_length=2)
    inputun=models.CharField(max_length=2)
    inputb=models.CharField(max_length=2)
    inputsp=models.CharField(max_length=2)
    inputbs=models.CharField(max_length=2)
    inputpc=models.CharField(max_length=2)
    inputht=models.CharField(max_length=2)
    inputhc=models.CharField(max_length=2)
    inputbt=models.CharField(max_length=2)
    inputo=models.CharField(max_length=2)
    ttl=models.CharField(max_length=2)