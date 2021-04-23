from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Administrador para perfiles de usuario"""

    def create_user(self, email: str, password: str):
        """Crea un nuevo usuario"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        """Crea un nuevo superusuario"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Clase que representa los usuarios en el sistema"""

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def get_full_name(self) -> str:
        """Retrieve full name of user"""

        return self.email

    def get_short_name(self) -> str:
        """Retrieve short name of user"""

        return self.email

    def __str__(self) -> str:
        """Return string representation of our user"""

        return self.email
