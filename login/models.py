from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name ='user_profile', on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')
    about_me = models.CharField(max_length=256,default='Hello buddy Welcome . Thanks for visiting my profile . Please send mail to conact me.')


    def __str__(self):
        return self.user
