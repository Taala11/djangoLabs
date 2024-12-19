from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length=100)  # City name

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)  # Student name
    age = models.IntegerField()  # Student age
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  # Link to Address

    def __str__(self):
        return self.name