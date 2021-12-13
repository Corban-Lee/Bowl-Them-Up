from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    # Creating a normal user
    def create_user(self, EmailAddress, username, password, **extra_fields):
        if not EmailAddress:
            raise ValueError(_('The Email must be set'))
        EmailAddress = self.normalize_email(EmailAddress)
        user = self.model(email=EmailAddress, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Creating a superuser
    def create_superuser(self, EmailAddress, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(EmailAddress, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    UserID       = models.AutoField(primary_key=True)
    FirstName    = models.CharField(max_length=64)
    LastName     = models.CharField(max_length=64)
    PhoneNumber  = models.CharField(max_length=10)
    EmailAddress = models.EmailField(max_length=128, unique=True)
    password     = models.CharField(max_length=64)
    is_staff     = models.BooleanField(_('staff'), default=False)
    is_active    = models.BooleanField(_('active'), default=True)

    # This tells django to use the email as the main sign in field.
    USERNAME_FIELD = 'EmailAddress'
    REQUIRED_FIELDS = [
        'FirstName',
        'LastName',
    ]

    def __str__(self):
        return self.FirstName + ' ' + self.LastName

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')