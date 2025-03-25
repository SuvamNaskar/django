from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    file = models.FileField()

class Car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)

    def __str__(self):
        return self.name


### *commands to migrate models
## python manage.py makemigration
## python manage.py migrate