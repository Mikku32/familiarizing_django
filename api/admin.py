from django.contrib import admin
from api.models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): 
    pass 
    #registering the student table in admin