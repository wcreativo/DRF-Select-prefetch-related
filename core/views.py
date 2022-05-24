from django.shortcuts import render

from .models import Book, Department, Employee


def home(request):
    employees = Employee.objects.all().select_related('department')
    for employee in employees:
        print(employee.name, employee.department.name)

def books(request):
    books = Book.objects.all().prefetch_related('stores_contain_it')
    for book in books:
        print(book.stores_contain_it.all())
    return None

def departments(request):
    departments_list = Department.objects.all().prefetch_related('employee_set')
    for department in departments_list:
        print(department.employee_set.all())
    return None


