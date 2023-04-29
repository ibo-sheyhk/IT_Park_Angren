from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    postal_code = models.CharField(max_length=70)
    about = models.TextField()
    avatar = models.ImageField(upload_to='user_profile')
    
    def __str__(self):
        return str(self.username)


class Employee(models.Model):
		full_name = models.CharField(max_length=100)
		birth_date = models.DateField()
		country = models.CharField(max_length=70)
		city = models.CharField(max_length=50)
		addres = models.CharField(max_length=50)
		image = models.ImageField(upload_to='employee')

		def __str__(self):
			return self.full_name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    specification = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teacher')