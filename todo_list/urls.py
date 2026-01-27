from django.urls import path

# from . import views
from .views import TaskListView,CreateTaskView
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path("login",LoginView.as_view(template_name='todo_list/login.html'), name="login"),
    path("logout",LogoutView.as_view(), name="logout"),
    path("task_list",TaskListView.as_view(), name="task_list"),
    path("create",CreateTaskView.as_view(), name="create_task"),
]
