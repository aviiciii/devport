from django.db import models

# Create your models here.
class Profile(models.Model):
    name= models.CharField(max_length=100)
    role= models.CharField(max_length=50, default='user')
    about= models.TextField(max_length=500, blank=True)
    college= models.CharField(max_length=100, blank=True)
    course= models.CharField(max_length=100, blank=True)
    grade= models.CharField(max_length=100, blank=True)
    graduation_year= models.CharField(max_length=100, blank=True)
    contact_email= models.CharField(max_length=100, blank=True)
    instagram= models.CharField(max_length=100, blank=True)
    linkedin= models.CharField(max_length=100, blank=True)
    twitter= models.CharField(max_length=100, blank=True)
    github= models.CharField(max_length=100, blank=True)

