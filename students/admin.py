from django.contrib import admin
from .models import Student
# Register your models here.
admin.site.register(Student)

def __str__(self):
    return f'Student: {self.first_name} {self.last_name}' 