from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True)

	REQUIRED_FIELDS = ['first_name', 'last_name']
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'

	objects = UserManager()

	def __str__(self):
		return self.email

	class Meta:
		ordering = ('-date_joined',)