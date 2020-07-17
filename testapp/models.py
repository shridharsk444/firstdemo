from django.db import models

# Create your models here.
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
   # phonenumber=models.IntegerField()
    adds=models.TextField()


