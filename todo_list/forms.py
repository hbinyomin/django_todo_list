from .models import Task
from django import forms
import re



class TaskForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        # Check for at least one character
        if not re.search(r"[A-Za-z]", title):
            raise forms.ValidationError(
                "Title must contain characters"
            )
        return title
    
    def clean_description(self):
        description = self.cleaned_data["description"].strip()

        # Check for at least one character
        if not re.search(r"[A-Za-z]", description):
            raise forms.ValidationError(
                "Description must contain characters"
            )
        return description

    class Meta:
        model = Task
        fields = ("title","description")