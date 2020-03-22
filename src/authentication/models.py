from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Расширенная версия базовой модели пользователя.

    Добавлено m2m-поле на других пользователей.
    """
    followers = models.ManyToManyField(
        'User',
        related_name='authors',
        verbose_name=_('followers')
    )

    def follow(self, author):
        """
        Метод для подписки на другого пользователя.

        В метод передаётся объект модели другого пользователя.
        Возвращает булеву переменную.
        """
        if self in author.followers.all():
            return False
        author.followers.add(self)
        return True

    def unfollow(self, author):
        """
        Метод для отписки от другого пользователя.

        Сигнатуры метода аналогичны методу `follow(author)`
        """
        if self in author.followers.all():
            author.followers.remove(self)
            return True
        return False

    def get_url(self):
        return reverse('user-detail', args=(self.username,))

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
