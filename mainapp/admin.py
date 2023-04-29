from django.contrib import admin
from .models import  Employee, Teacher, UserProfile

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Employee)
admin.site.register(Teacher)
