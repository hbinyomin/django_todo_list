from .models import Task
from django import forms



class TaskForm(forms.ModelForm):

    # title = forms.CharField(
    #     max_length=20,
    #     required=True,
    #     error_messages={"required": "Title needs to have a value"}
    # )
    # description = forms.CharField(
    #     max_length=20,
    #     required=True,
    #     error_messages={"required": "Title needs to have a value"}
    # )

    class Meta:
        model = Task
        fields = ("title","description")