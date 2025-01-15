from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_kwargs):
		email = self.normalize_email(email=email)
		user = self.model(email=email, **extra_kwargs)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_kwargs):
		extra_kwargs.setdefault('is_staff', True)
		extra_kwargs.setdefault('is_superuser', True)
		return self.create_user(email, password, **extra_kwargs)