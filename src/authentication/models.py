from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # Подписчики
    followers = models.ManyToManyField(
        'User',
        related_name='authors',
        verbose_name=_('followers')
    )

    def follow(self, author):
        if self in author.followers.all():
            return False
        author.followers.add(self)
        return True

    def unfollow(self, author):
        if self in author.followers.all():
            author.followers.remove(self)
            return True
        return False

    def get_url(self):
        return reverse('user-detail', args=(self.username,))

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
