from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=250,null=False,blank=False)
    