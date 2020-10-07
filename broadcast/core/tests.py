from django.contrib import auth
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient


class UserTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = "test_user"
        self.password = "test_password"

    def test_login_user(self):
        user = User.objects.create_user(
            username=self.username, password=self.password)
        self.assertTrue(self.client.login(
            username='test_user', password='test_password'))

        self.assertEqual(response.status_code, 200)
