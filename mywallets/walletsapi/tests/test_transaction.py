from rest_framework import status
from rest_framework.test import APITestCase
from walletsapi.models import Wallet, User


class TransactionsTestCase(APITestCase):
    def setUp(self) -> None:
        url = "/auth/users/"
        user1 = {
            "email": "test1@test.com",
            "username": "testuser1",
            "password": "HelloTest3",
        }
        user2 = {
            "email": "test2@test.com",
            "username": "testuser2",
            "password": "HelloTest4",
        }
        user3 = {
            "email": "test2@test.com",
            "username": "testuser3",
            "password": "HelloTest5",
        }
        self.client.post(url, user1, format="json")
        self.client.post(url, user2, format="json")
        self.client.post(url, user3, format="json")

        data = {"type": "VISA", "currency": "USD"}
        self.client.login(username="testuser1", password="HelloTest3")
        self.client.post("/wallets/", data, format="json")
        self.client.logout()

        self.client.login(username="testuser2", password="HelloTest4")
        self.client.post("/wallets/", data, format="json")
        self.client.logout()

        data_EUR = {"type": "VISA", "currency": "EUR"}
        self.client.login(username="testuser3", password="HelloTest5")
        self.client.post("/wallets/", data_EUR, format="json")
        self.client.logout()

        self.user1 = User.objects.get(id=1)
        self.user2 = User.objects.get(id=2)
        self.user3 = User.objects.get(id=3)
        self.wallet_user1 = Wallet.objects.get(user_id=self.user1.id)
        self.wallet_user2 = Wallet.objects.get(user_id=self.user2.id)
        self.wallet_user3 = Wallet.objects.get(user_id=self.user3.id)

    def test_create_transaction(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user2}",
            "transfer_amount": "2.00",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data['status'], 'PAID')

    def test_positive_balance(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user2}",
            "transfer_amount": "5.00",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data, {"detail": "not enough money"})

    def test_for_same_currency(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user3}",
            "transfer_amount": "2.00",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.data,
                         {"detail": "transactions are available only for wallets with the same currency"})

    def test_get_users_transaction(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data1 = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user2}",
            "transfer_amount": "1.00",
        }
        data2 = {
            "sender": f"{self.wallet_user2}",
            "receiver": f"{self.wallet_user1}",
            "transfer_amount": "4.00",
        }
        self.client.post(url, data1, format="json")
        self.client.post(url, data2, format="json")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

    def test_get_transaction_by_id(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data1 = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user2}",
            "transfer_amount": "1.00",
        }
        data2 = {
            "sender": f"{self.wallet_user2}",
            "receiver": f"{self.wallet_user1}",
            "transfer_amount": "4.00",
        }
        self.client.post(url, data1, format="json")
        self.client.post(url, data2, format="json")
        response = self.client.get(url)
        new_url = f"/wallets/transactions/{response.data[1]['id']}/"
        new_response = self.client.get(new_url)
        self.assertEqual(new_response.data['status'], 'PAID')

    def test_get_transaction_where_wallet_was_sender_or_receiver(self):
        self.client.login(username="testuser1", password="HelloTest3")
        url = "/wallets/transactions/"
        data1 = {
            "sender": f"{self.wallet_user1}",
            "receiver": f"{self.wallet_user2}",
            "transfer_amount": "1.00",
        }
        data2 = {
            "sender": f"{self.wallet_user2}",
            "receiver": f"{self.wallet_user1}",
            "transfer_amount": "4.00",
        }
        self.client.post(url, data1, format="json")
        self.client.post(url, data2, format="json")
        response = self.client.get(url)
        new_url = f"/wallets/transactions/{response.data[1]['sender']}/"
        new_response = self.client.get(new_url)
        self.assertEqual(len(new_response.data), 2)
