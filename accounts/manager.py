from django.contrib.auth.models import BaseUserManager 

from django.utils.translation import gettext_lazy as _          # ?????



class CustomUserManager(BaseUserManager):
    """ 
    Custom User Manager 
    Email is the unique identifier for the authentication.
    """

    # Create an ordinary User
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('You need to provide an Email address.')
         
        email = self.normalize_email(email)                                 # ??????
        user = self.model(email=email, username=username, **extra_fields)   # ????
        user.set_password(self.cleaned_data['password'])                    # ?????     
        user.save()
        return user


    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to as_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned to as_superuser=True'))
        
        return self.create_user(username, email, password, **extra_fields)
        





