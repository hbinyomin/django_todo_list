from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    def handle(self,*args, **kwargs):
        users = [
            {'username':'ruvain', 'password':'go'},
            {'username':'chaim', 'password':'go'}
        ]

        for u in users:
            user = User.objects.create_user(username=u.get('username'), password=u.get('password'))
            print(f'Created new User: {user.username}')
    