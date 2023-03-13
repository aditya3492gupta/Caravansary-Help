from django.db import models

# Create your models here.
class food_enquiry(models.Model):
    name=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    date=models.DateField()
    time=models.CharField(max_length=20)
    reason=models.TextField()

class services(models.Model): 
    name=models.CharField(max_length=50)
    email=models.EmailField()
    room=models.CharField(max_length=50)
    message=models.TextField()