from django.db import models

# Create your models here.

# Create your models here.

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ManyToManyField(Department,blank=True)
