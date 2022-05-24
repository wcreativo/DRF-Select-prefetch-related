from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('departments/', views.departments, name='departments'),
]
