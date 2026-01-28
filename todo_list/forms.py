from .models import Task
from django import forms
import re


class TaskForm(forms.ModelForm):
    
    CONFIG_TYPE_CHOICES = [
        ('string', 'String'),
        ('number', 'Number'),
        ('boolean', 'Boolean'),
    ]

    configurable_type = forms.ChoiceField(choices=CONFIG_TYPE_CHOICES, label="Data Type")
    configurable_value = forms.CharField(required=False, label="Value")

    
    class Meta:
        model = Task
        fields = ("title","description")
    
    def clean(self):
        cleaned_data = super().clean()
        
        configurable_type = cleaned_data.get('configurable_type')
        configurable_value = cleaned_data.get('configurable_value')

        if configurable_type=='string':
            # This validation could have been acheived via required=True on the field, but used this way for clarity. Both would result in double error messages.
            # CharField strips whitespace, so stripping whitespace not needed here to prevent "  " being saved, even without the regex below.
            if not configurable_value:
                self.add_error("configurable_value","Some value is required")
            elif not re.search(r"[A-Za-z]", configurable_value):
                self.add_error("configurable_value","Please enter a string with characters")
            else:
                cleaned_data['configurable_value']=str(configurable_value)
            
        elif configurable_type=="number":
            try:
                cleaned_data["configurable_value"] = float(configurable_value)
            except (ValueError,TypeError):
                # TypeError is needed for Null; CharField should prevent, but extra level of secuirty
                self.add_error("configurable_value","A valid number is required")
        
        elif configurable_type=="boolean":
            if configurable_value.lower() in ['true','t']:
                cleaned_data["configurable_value"]=True
            elif configurable_value.lower() in ['false','f']:
                cleaned_data["configurable_value"]=False
            else:
                self.add_error("configurable_value","You must enter True/T or False/F")
        
        return cleaned_data
    
    def clean_title(self):
        title = self.cleaned_data["title"]

        # Check for at least one character
        if not re.search(r"[A-Za-z]", title):
            raise forms.ValidationError(
                "Title must contain characters"
            )
        return title
    
    def clean_description(self):
        description = self.cleaned_data["description"]

        # Check for at least one character
        if not re.search(r"[A-Za-z]", description):
            raise forms.ValidationError(
                "Description must contain characters"
            )
        return description
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.configurable = {
            "configurable_type": self.cleaned_data['configurable_type'],
            "configurable_value": self.cleaned_data['configurable_value'],
        }

        if commit:
            instance.save()
        
        return instance
