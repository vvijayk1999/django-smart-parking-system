from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
'''class UserDetails(models.Model):
    user_name = models.TextField()
    email = models.TextField()
    v_id = models.TextField(max_length = 10)
    password = models.TextField()
    def __str__(self):
        return '%s' % self.user_name'''
class UserDetail(models.Model):
    user_name = models.TextField()
    email = models.TextField()
    v_id = models.TextField(max_length = 10)
    password = models.TextField()
    password2 = models.TextField()

    def __str__(self):
        return '%s' % self.user_name 