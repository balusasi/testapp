from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    gender_choices=(('M', 'Male'),('F', 'Female'),)
    gender=models.CharField(max_length=1,choices=gender_choices)
