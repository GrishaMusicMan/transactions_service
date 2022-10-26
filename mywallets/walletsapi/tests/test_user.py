from rest_framework import status
from rest_framework.test import APITestCase


class CreateUserTestCase(APITestCase):

    def test_create_user(self):
        url = "/auth/users/"
        data = {
            "email": "test@gmail.com",
            "username": "test",
            "password": "HelloTest1",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        url = "/auth/users/"
        data = {
            "email": "test@gmail.com",
            "username": "test",
            "password": "HelloTest1",
        }
        self.client.post(url, data, format="json")
        login_response = self.client.login(username="test", password="HelloTest1")
        self.assertEqual(login_response, True)