from django.db import models

# Create your models here.

class Student(models.Model): 
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)
    #create table Student(name varchar(100),roll integer,course varchar(100))

    def __str__(self) :
        return self.name   #for easier access,not necessary
