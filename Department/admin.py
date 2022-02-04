from django.contrib import admin
from . models import Department, Students
from Department import models

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name']


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id','first_name']