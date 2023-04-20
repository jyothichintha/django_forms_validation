from django.db import models

# Create your models here.
class Student_details(models.Model):
    sid=models.IntegerField(primary_key=100)
    sname=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name