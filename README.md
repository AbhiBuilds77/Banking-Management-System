# 🏦 Advanced Banking Management System

A Python-based console application that simulates core banking operations using Object-Oriented Programming principles.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [OOP Concepts Used](#oop-concepts-used)
- [Project Structure](#project-structure)
- [Classes Overview](#classes-overview)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Limitations](#limitations)
- [Future Scope](#future-scope)

---

## About the Project

The **Advanced Banking Management System** is a menu-driven Python application that simulates real-world banking operations. Built entirely with Python's OOP approach in a single file, it handles multiple accounts, secure transactions, and maintains a complete transaction history — all without any external dependencies.

---

## Features

### Basic
- Create new bank account
- Deposit money
- Withdraw money
- Check account balance
- View all accounts

### Advanced
- Transfer money between accounts
- Transaction history tracking (per account + bank-wide)
- Encapsulated (private) balance for security
- Error handling for invalid inputs and insufficient balance
- Auto-generated 10-digit account numbers

---

## OOP Concepts Used

| Concept | Implementation |
|---|---|
| **Class** | `Account`, `Bank`, `Transaction` |
| **Object** | `obj1`, `obj2`, `bank`, `transaction_obj` |
| **Constructor** | `__init__()` in all classes |
| **Encapsulation** | `__balance` is a private variable |
| **Inheritance** | `SavingsAccount`, `CurrentAccount` extend `Account` |
| **Polymorphism** | `withdraw()` behaves differently per account type |
| **Abstraction** | User interacts only via menu; internal logic is hidden |
| **Composition** | `Bank` contains a list of `Account` objects |
| **Exception Handling** | Handles `ValueError`, insufficient balance, account not found |

---

## Project Structure

```
banking_system.py        ← Single file containing all classes and logic
README.md
```

### System Architecture

```
            BANK SYSTEM
                 |
    --------------------------------
    |                              |
 ACCOUNT                      TRANSACTION
    |
--------------------
|                  |
SavingsAccount  CurrentAccount
```

---

## Classes Overview

### `Account` (Base Class)
Defines the core structure for all bank accounts.

| Member | Description |
|---|---|
| `name` | Account holder's name |
| `account_no` | Unique account identifier |
| `__balance` | Private balance (encapsulated) |
| `transactions` | List of account-level transaction records |
| `deposit(amount, timestamp)` | Adds money to balance |
| `withdraw(amount, timestamp)` | Deducts money if balance is sufficient |
| `transfer_money(amount, other, timestamp)` | Transfers funds to another account |
| `get_balance()` | Returns current balance |
| `transation_history()` | Prints all transactions for this account |

---

### `Bank` (Controller Class)
Manages all accounts in the system.

| Member | Description |
|---|---|
| `accounts` | List of all `Account` objects |
| `create_account(account)` | Registers a new account |
| `show_accounts()` | Displays all accounts with balance |
| `find_account(account_no)` | Searches and returns an account by number |

---

### `Transaction` (Record Class)
Tracks all bank-level transaction events.

| Member | Description |
|---|---|
| `bank_transactions` | List of all bank-wide transactions |
| `bank_transaction_update(type, amount, time)` | Logs a new transaction |
| `bank_transation_history()` | Prints full bank transaction log |

---

## How to Run

**Requirements:** Python 3.10 or higher (uses `match-case` syntax)

```bash
# Clone or download the project
python banking_system.py
```

No external libraries required. Only standard library modules (`datetime`, `random`) are used.

---

## Usage

On running the script, a menu is displayed:

```
Menu:
 1. Create Account
 2. Deposit Money
 3. Withdraw Money
 4. Transfer Money
 5. Check Balance
 6. Show All Accounts
 7. Transaction History
 8. Exit
```

Enter the number corresponding to the operation you want to perform.

---

## Sample Output

```
Choose Option: 1
Enter Name: Rahul
Enter Initial Balance: 10000
Account created successfully! Your Account Number is: 4738291056

Choose Option: 2
Enter Amount: 5000
Transaction Successful

Choose Option: 5
Your balance is: 15000

Choose Option: 7
--- Personal Transaction History ---
Deposited 5000 at 2025-06-01 10:45:32
```

---

## Limitations

- Data is not saved permanently (no file/database storage)
- No GUI interface
- Menu is currently hardcoded to operate on `obj1` (chintu's account) for deposit, withdraw, and transfer

---

## Future Scope

- Add file handling to persist account data across sessions
- Build a GUI using Tkinter
- Implement a login/authentication system
- Add ATM simulation mode
- Integrate a database (SQLite) for permanent storage
- Complete `SavingsAccount` and `CurrentAccount` subclass implementations

---

## Author

Developed as a Python OOP academic project demonstrating core software engineering and object-oriented design principles.
