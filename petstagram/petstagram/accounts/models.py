from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db import models

from petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    '''
    AbstractUser raises exception models.E006 superuser fields clashes
    '''

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )  # needed for create user manager

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )  # fixes date join exception

    USERNAME_FIELD = 'email'

    object = PetstagramUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,  # because is automatically created after save (signal)
    )
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
