import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password, email, first_name, last_name, **stuff):

        stuff.setdefault('is_staff', True)
        stuff.setdefault('is_superuser', True)
        stuff.setdefault('is_active', True)

        if stuff.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if stuff.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, password, email, first_name, last_name, **stuff)

    def create_user(self, username, password, email, first_name, last_name, **stuff):

        if not email:
            raise ValueError('You must provide an email address')

        user = self.model(username=username,
                          password=password,
                          email=email,
                          first_name=first_name,
                          last_name=last_name,
                          **stuff)
        user.set_password(password)
        user.save(using=self.db)
        return user


class CustomeUsers(AbstractBaseUser, PermissionsMixin):
    """
    Model customuser
    """

    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, unique=True)
    start_date = models.DateField(default=datetime.date.today)

    first_name = models.CharField('first name', max_length=50, default="")
    last_name = models.CharField('last name', max_length=50, default="")

    about = models.TextField('about', max_length=500, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'email', 'last_name']

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"
