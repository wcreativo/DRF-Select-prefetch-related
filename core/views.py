from django.shortcuts import render

from .models import Book, Employee


def home(request):
    employees = Employee.objects.all().select_related('department')
    for employee in employees:
        print(employee.name, employee.department.name)

def books(request):
    books = Book.objects.all().prefetch_related('stores_contain_it')
    for book in books:
        print(book.stores_contain_it.all())
    return None


