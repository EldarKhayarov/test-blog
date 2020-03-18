from django.db import models
from django.contrib.auth import get_user_model
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Post title'))
    text = models.TextField(max_length=1000, verbose_name=_('Post text'))
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name=_('Author of the post')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date of creation')
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class PostIsRead(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    @cached_property
    def author(self):
        return self.post.author
