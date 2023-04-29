# from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2',]  
        
        
# class CreateMentorForm(forms.ModelForm):
#   class Meta:
#     model = Mentor
#     fields = ['first_name','last_name','gender','default','birth_date','spesification','choices']
    
    
class CreateEmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = ['full_name','birth_date','country','city','addres',]