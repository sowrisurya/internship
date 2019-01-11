from django.db import models
from django.contrib.auth.models import User

class userspec(models.Model):
    types = (
        ('seller','seller'),
        ('user','user'),
        ('clinic','clinic'),
        ('hospital','hospital'),
        ('bloodbank','bloodbank'),
        ('diagnostic','diagnostic'),
    )
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=types, default='user')
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.username