from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    username = models.CharField(max_length=40,unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    objects = UserManager()

    def __str__(self):
        return self.username


