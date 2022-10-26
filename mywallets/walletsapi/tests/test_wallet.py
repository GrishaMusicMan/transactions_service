from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class WalletApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            username="testuser",
            password="HelloTest2",
        )
        self.client.force_authenticate(self.user)

    def test_create_wallet(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wallets(self):
        url = "/wallets/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wallets_wathout_login(self):
        self.client.logout()
        url = "/wallets/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_more_five_wallets(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        for i in range(5):
            self.client.post(url, data, format="json")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data, {"detail": "you can't have more than 5 wallets"})

    def test_getting_start_cash(self):
        url = "/wallets/"
        data1 = {"type": "VISA", "currency": "USD"}
        data2 = {"type": "VISA", "currency": "EUR"}
        data3 = {"type": "VISA", "currency": "UAH"}
        response1 = self.client.post(url, data1, format="json")
        response2 = self.client.post(url, data2, format="json")
        response3 = self.client.post(url, data3, format="json")
        self.assertEqual(response1.data['balance'], '3.00')
        self.assertEqual(response2.data['balance'], '3.00')
        self.assertEqual(response3.data['balance'], '100.00')

    def test_get_wallet_by_name(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.post(url, data, format="json")
        name = response.data['name']
        new_url = f'/wallets/{name}/'
        new_response = self.client.get(new_url)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test_delete_wallet(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.post(url, data, format="json")
        name = response.data['name']
        new_url = f'/wallets/{name}/'
        new_response = self.client.delete(new_url)
        self.assertEqual(new_response.data, {"delete": "success"})

    def test_delete_wallet_without_login(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.post(url, data, format="json")
        name = response.data['name']
        new_url = f'/wallets/{name}/'
        self.client.logout()
        new_response = self.client.delete(new_url)
        self.assertEqual(new_response.data, {"detail": "Учетные данные не были предоставлены."})

    def test_put_wallet(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_wallet(self):
        url = "/wallets/"
        data = {"type": "VISA", "currency": "USD"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
