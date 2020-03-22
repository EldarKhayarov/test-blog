from django.core.mail import send_mass_mail
from django.contrib.auth import get_user_model
from django.conf import settings

from . import utils


User = get_user_model()


def get_followers_list(author: User):
    """
    Функция, возвращающая список email'ов подписчиков.
    """
    return author.followers.values_list('email', flat=True).all()


def datatuple_generator(subject, message, from_email, recipients):
    for r in recipients:
        yield subject, message, from_email, (r,)


def create_post_mass_mail(title, author):
    generator = datatuple_generator(
        'Оповещение',
        utils.post_created_template(title, author.username),
        settings.EMAIL_HOST_USER,
        get_followers_list(author)
    )
    send_mass_mail(generator)


def update_post_mass_mail(title, author):
    generator = datatuple_generator(
        'Оповещение',
        utils.post_updated_template(title, author.username),
        settings.EMAIL_HOST_USER,
        get_followers_list(author)
    )
    return generator


def delete_post_mass_mail(title, author):
    generator = (
        'Оповещение',
        utils.post_deleted_template(title, author.username),
        settings.EMAIL_HOST_USER,
        get_followers_list(author)
    )
    return generator
