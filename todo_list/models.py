from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=250,null=False,blank=False)
    # completed = models.BooleanField(default=False,null=False,blank=False)

    # def __str__(self):
    #     return self.title
