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
