from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()

USER1 = {
    'USERNAME': 'user1',
    'EMAIL': 'user1@user.com',
    'PASSWORD': 'JKJDE3RRJIJF'
}

USER2 = {
    'USERNAME': 'user2',
    'EMAIL': 'user2@user.com',
    'PASSWORD': 'JKJDE3RRJIJF'
}

USER3 = {
    'USERNAME': 'user3',
    'EMAIL': 'user3@user.com',
    'PASSWORD': 'JKJDE3RRJIJF'
}


# TODO: добавить пару тестов
