from django.views.generic import ListView,CreateView,TemplateView

from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(TemplateView):
    template_name='todo_list/login.html'

class TaskListView(LoginRequiredMixin,ListView):
    template_name = "todo_list/task_list.html"
    model = Task
    context_object_name="tasks"

class CreateTaskView(LoginRequiredMixin,CreateView):
    model=Task
    # fields=['title','description']
    form_class=TaskForm
    template_name="todo_list/create_task.html"
    success_url=reverse_lazy('task_list')


# Authentication, sign-in required

# Each to-do item must include a configurable field that supports three data types (for example: string, boolean, and number)

# Each data type must have appropriate validation, Validation should be enforced on both the frontend and backend

# Submitted to-do items should be saved persistently and retrievable after refresh/login


# butto for Create New item
# form for creating new item