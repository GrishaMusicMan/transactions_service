## Transactions service  💰
 
### Description:
- API for financial operations. Input and output data - JSON format.
- Each user can create no more than five wallets with different currencies: USD, EUR, UAH.
- Transactions are available only for wallets with the same currency. 
  USD to USD - avalible, EUR to USD - unvalible.
- Сommission between wallets of different users is 10%, between wallets of one user - 0%.
- Start bonus from our API service for new wallet 3 EUR or USD or 100 UAH

### Install dependency:
```
pip install -r requirements.txt
```
### Run tests:
```
python manage.py test walletsapi.tests
```
### How to use:
- Create User:
  - POST `/auth/users/` 
  ```
  {
      "email": "example@gmail.com",
      "username": "name",
      "password": "password"
  }
  ```
- Login:
  - POST `/auth/token/login` 
  ```
  {
      "username": "name",
      "password": "password"
  }
  ```
- Create wallet:
  - POST `/wallets/` 
  ```
  {
      "type": "VISA",
      "currency": "USD"
  }
  ```
- Get all users wallets:
  - GET `/wallets/` 

- Get wallet by name:
  - GET `/wallets/<NAME>`
- Delete wallet:
  - DELETE `/wallets/<NAME>` 
- Create new transaction:
  - POST `/wallets/` 
  ```
  {
      "sender": "45JFKJ4",
      "receiver": "KJ3K4JD",
      "transfer_amount": "100.00"
  }
  ```
- Get all transactions for current user:
  - GET `/wallets/transactions/` 
- Get transaction by <transaction_id>:
  - GET `/wallets/transactions/<transaction_id>/` 
- Get all transactions where wallet was sender or receiver:
  - GET `/wallets/transactions/<wallet_name>/` 

## curl:
- Get all users wallets:
```
curl --location --request GET 'http://127.0.0.1:8000/wallets/' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```
- Create wallet:
```
curl --location --request POST 'http://127.0.0.1:8000/wallets/' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122' \
--header 'Content-Type: application/json' \
--data-raw '{
	"type": "VISA",
	"currency": "USD"
}'
```
- Get wallet by name:
```
curl --location --request GET 'http://127.0.0.1:8000/wallets/3YS60MNP' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```
- Delete wallet:
```
curl --location --request DELETE 'http://127.0.0.1:8000/wallets/3456NJCQ' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```
- Get all transactions for current user:
```
curl --location --request GET 'http://127.0.0.1:8000/wallets/transactions' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```
- Get transaction by <transaction_id>:
```
curl --location --request GET 'http://127.0.0.1:8000/wallets/transactions/24' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```
- Get all transactions where wallet was sender or receiver:
```
curl --location --request GET 'http://127.0.0.1:8000/wallets/transactions/20U7YF0D' \
--header 'Authorization: Token ff246e3a0052f383b62f3746200238744f7ae122'
```