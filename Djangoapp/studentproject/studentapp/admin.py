from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','gender']
admin.site.register(Student,StudentAdmin)

# Register your models here.
