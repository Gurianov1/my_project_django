from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Person(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Children(models.Model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pet(models.Model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

    def __str__(self):
        return self.name