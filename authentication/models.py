from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class AccountManager(UserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        super().create_user(username, password=password, email=email, **kwargs)

    def create_superuser(self, username, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        super().create_superuser(
            username, password=password, email=email, **kwargs
        )


class Account(AbstractUser):
    tagline = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
Account._meta.get_field('email')._unique = True
