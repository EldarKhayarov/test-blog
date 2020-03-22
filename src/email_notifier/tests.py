from django.test import TestCase
from django.contrib.auth import get_user_model

from .mail import get_followers_list


User = get_user_model()


USER1 = {
    'username': 'user1',
    'email': 'user1@user.com',
    'password': 'useruser'
}

USER2 = {
    'username': 'user2',
    'email': 'user2@user.com',
    'password': 'useruser'
}

USER3 = {
    'username': 'user3',
    'email': 'user3@user.com',
    'password': 'useruser'
}

USER4 = {
    'username': 'user4',
    'email': 'user4@user.com',
    'password': 'useruser'
}


class EmailListTestCase(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(**USER1)
        self.user2 = User.objects.create_user(**USER2)
        self.user3 = User.objects.create_user(**USER3)
        self.user4 = User.objects.create_user(**USER4)
        self.user1.followers.add(self.user2.id)
        self.user1.followers.add(self.user3.id)

    def test_get_follwers_email_list(self):
        """
        Протестируем правильность вывода списка email'ов подписчиков.
        """
        emails = get_followers_list(self.user1)
        right_emails = ['user2@user.com', 'user3@user.com']
        TestCase.assertEqual(self, len(emails), len(right_emails))
        for email, right_email in zip(emails, right_emails):
            TestCase.assertEqual(self, email, right_email)

    def test_get_followers_empty_list(self):
        """
        Допустим, подписчиков нет.
        """
        self.user1.followers.clear()
        emails = get_followers_list(self.user1)
        TestCase.assertEqual(self, len(emails), 0)
