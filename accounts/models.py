from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class User(AbstractUser):
    bio = models.CharField(_("Bio"), max_length=500)
    email = models.EmailField(_('email address'), unique=True, null=True)

    class Meta:
        db_table = 'User'
        verbose_name = _("User")
        verbose_name_plural = _("Users")