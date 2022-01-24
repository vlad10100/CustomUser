from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.utils.translation import gettext_lazy as _ 


from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Customize User model by overridding AbstractBaseUser
    User will have to provide:
            first_name
            last_name
            birthday
            username
            email
            password
    """

    # User Details
    first_name      = models.CharField(_('First Name'), max_length=30)
    last_name       = models.CharField(_('Last Name'), max_length=30)
    birthday        = models.DateField(_('Birthday'), blank=True, null=True)
    username        = models.CharField(_('Username'), max_length=15, unique=True)
    email           = models.EmailField(_('Email'), unique=True)


    # User Status
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    date_created    = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']    
    

    objects = CustomUserManager()


    class Meta:
        verbose_name = 'ACCOUNTS'
        verbose_name_plural = 'ACCOUNTS'


    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name