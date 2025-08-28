from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="salem", email="salem@test.com", password="testpass123")
        self.assertEqual(user.username, "salem")
        self.assertTrue(user.check_password("testpass123"))


# Create your tests here.
