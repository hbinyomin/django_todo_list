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

    def get_form(self,form_class=None):
        form = super().get_form(form_class)

        order = self.request.GET.get("order") or self.request.session.get("field_order", "default")

        self.request.session["field_order"] = order

        if order == 'description':
            form.order_fields([
                "description",
                "title",
                "configurable_type",
                "configurable_value",  
            ])
        else:
            form.order_fields([
                "title",
                "description",
                "configurable_type",
                "configurable_value",  
            ])

        return form


