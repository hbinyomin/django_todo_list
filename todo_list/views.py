from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# Create your views here.

class IndexView(ListView):
    template_name = "todo_list/task_list.html"
    model = Task
    context_object_name="tasks"

#

# Authentication, sign-in required
# 
# Data types and models
# To Do list
# butto for Create New item
# form for creating new item
# Each to-do item must include a configurable field that supports three data types (for example: string, boolean, and number)
# Each data type must have appropriate validation, Validation should be enforced on both the frontend and backend
# Submitted to-do items should be saved persistently and retrievable after refresh/login