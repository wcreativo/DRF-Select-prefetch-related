from django.contrib import admin

from .models import Book, Department, Employee, Store

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Book)
admin.site.register(Store)
