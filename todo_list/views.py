from django.views.generic import ListView,CreateView,TemplateView

from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(TemplateView):
    template_name='todo_list/login.html'

class TaskListView(LoginRequiredMixin,ListView):
    template_name = "todo_list/task_list.html"
    model = Task
    context_object_name="tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class CreateTaskView(LoginRequiredMixin,CreateView):
    model=Task
    form_class=TaskForm
    template_name="todo_list/create_task.html"
    success_url=reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Authentication, sign-in required

# Each to-do item must include a configurable field that supports three data types (for example: string, boolean, and number)

# Each data type must have appropriate validation, Validation should be enforced on both the frontend and backend

# Submitted to-do items should be saved persistently and retrievable after refresh/login
