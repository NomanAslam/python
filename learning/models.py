from django.db import models

class University(models.Model):
    uniName = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)

class Student(models.Model):
    name = models.CharField(max_length=100)
    standard = models.IntegerField()
    age = models.IntegerField(default=18)
    #university = models.ForeignKey(University, on_delete=models.CASCADE)

class Teacher(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    age = models.IntegerField()
    #students = models.ManyToManyField(Student)

class Drink(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    quality = models.IntegerField(default=1)

    def __str__(self):
        return self.name + ' ' + self.description

    
