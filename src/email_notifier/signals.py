from django.db.models.signals import (
    post_save,
    pre_delete,
)
from django.dispatch import receiver

from blog.models import Post
from .mail import (
    create_post_mass_mail,
    update_post_mass_mail,
    delete_post_mass_mail,
)


@receiver(post_save, sender=Post, dispatch_uid='create_update_post_notifier')
def create_update_post_notifier(sender, instance, created, **kwargs):
    if created:
        create_post_mass_mail(instance.title, instance.author)
    else:
        update_post_mass_mail(instance.title, instance.author)


@receiver(pre_delete, sender=Post, dispatch_uid='delete_post_notifier')
def delete_post_notifier(sender, instance, **kwargs):
    delete_post_mass_mail(instance.title, instance.author)


