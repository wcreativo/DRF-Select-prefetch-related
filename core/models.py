from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='stores_contain_it')

    def __str__(self) -> str:
        return self.name
