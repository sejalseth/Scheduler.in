from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainView, name='view'),
    path('addTodo', views.addTodo, name='addtodo'),
    path('addTask', views.addTask, name='addTask'),
    path('deleteTask/<int:todo_id>', views.deleteTask, name='deleteTask'),
]