from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    contact = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id} - {self.name}"