## Python Bank System

This project implements a basic bank system in Python, allowing users to perform deposits, withdrawals, and view their account statement. It's designed for educational purposes and simplicity, and doesn't include features like multiple accounts, security, or database storage.

### Features

* **Deposit:** Users can deposit positive amounts into their account.
* **Withdraw:** Users can withdraw money, with a daily limit of $500 and a maximum of 3 withdrawals per day.
* **Extract:** Users can view their transaction history and current balance.

### Requirements

* Python 3.x

### Running the Script

1. **Clone the repository:**

   ```bash
   git clone https://your-github-username/python-bank-system.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd python-bank-system
   ```

3. **Run the script:**

   ```bash
   python main.py
   ```

### Usage

The script will display a menu with these options:

* **d:** Deposit
* **s:** Withdraw
* **e:** Extract
* **q:** Exit

Choose an option and follow the prompts for the corresponding action.

### Example

```
Deposit
Value of deposit: 100
-------- Success deposit ! Balance: 100.00 --------

Withdraw
Value of withdraw: 50
-------- Withdraw successful ! Balance: 50.00 --------

Extract
Deposit: +100.00
Withdraw: -50.00
Current Balance: R$50.00

Exit
Thank you for using our bank!
```

### Limitations

* Single-user system, doesn't support multiple accounts.
* No security measures to protect user data.
* Transactions are not stored and lost upon script termination.

### Future Improvements

* Implement support for multiple accounts.
* Add security features like password protection and transaction verification.
* Store transactions in a database for persistence.
* Enhance the user interface with visual elements and error handling.

