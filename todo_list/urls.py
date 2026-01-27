from django.urls import path

# from . import views
from .views import TaskListView,CreateTaskView

urlpatterns = [
    # path("",LoginView.as_view(), name="login"),
    path("list",TaskListView.as_view(), name="task_list"),
    path("create",CreateTaskView.as_view(), name="create_task"),
]
