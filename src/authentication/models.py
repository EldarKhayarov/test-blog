from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Подписчики
    followers = models.ManyToManyField(
        'User',
        related_name='authors',
        verbose_name=_('followers')
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
