from datetime import datetime
import random

class Account:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no  #
        self.__balance = balance
        self.transactions = []

    def deposite(self, amount, timestamp):
        self.__balance += amount
        self.transactions.append(f"Deposited {amount} at {timestamp}")   

    def withdraw(self, amount, timestamp):
        if amount > self.__balance:
            print("Insufficient Balance")
            return False  
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdraw {amount} at {timestamp}")  
            return True

    def get_balance(self):
        return self.__balance
    
    def transfer_money(self, amount, other, timestamp):
        if amount > self.__balance:
            print("Insufficient Balance")
            return False
        else:
            
            other.deposite(amount, timestamp) 
            self.__balance -= amount   
            self.transactions.append(f"Money Transfer {amount} to {other.name} at {timestamp}")  
            return True

    def transation_history(self):
        if not self.transactions:
            print("No transactions found.")
        for transaction in self.transactions:
            print(transaction)        


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)    

    def show_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        for acc in self.accounts:
            print(f"Name: {acc.name} | Account No: {acc.account_no} | Balance: {acc.get_balance()}")

    def find_account(self, account_no):

        for acc in self.accounts:
            if acc.account_no == account_no:
                return acc
        return None

       
class Transaction:
    def __init__(self):
        self.bank_transactions = []

    def bank_transaction_update(self, transaction_type, amount, timestamp):
        self.bank_transactions.append(f"{transaction_type} {amount} at {timestamp}") 

    def bank_transation_history(self):
        for transaction in self.bank_transactions:
            print(transaction) 


# Setup initial data
bank = Bank()
obj1 = Account("chintu", 1234567890, 656656545)
obj2 = Account("pintu", 9876543210, 658699680)


bank.create_account(obj1)
bank.create_account(obj2)

transaction_obj = Transaction()

while True:
    print("\nMenu:\n 1. Create Account\n 2. Deposit Money\n 3. Withdraw Money\n 4. Transfer Money\n 5. Check Balance\n 6. Show All Accounts \n 7. Transaction History \n 8. Exit")
    try:
        option = int(input("Choose Option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match option:
        case 1: 
            name = input("Enter Name: ")
            account_no = random.randint(10**9, (10**10) - 1)
            balance = int(input("Enter Initial Balance: "))
            obj = Account(name, account_no, balance)
            bank.create_account(obj)  
            print(f"Account created successfully! Your Account Number is: {account_no}")
            
        case 2:
            amount = int(input("Enter Amount: "))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            obj1.deposite(amount, timestamp)
            transaction_obj.bank_transaction_update("Deposited", amount, timestamp)
            print("Transaction Successful")
            
        case 3:
            amount = int(input("Enter Amount: "))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if obj1.withdraw(amount, timestamp):
                transaction_obj.bank_transaction_update("Withdraw", amount, timestamp) 
                print("Transaction Successful")   
                
        case 4:
            amount = int(input("Enter Amount: "))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if obj1.transfer_money(amount, obj2, timestamp):
                transaction_obj.bank_transaction_update("Money Transfer", amount, timestamp)    
                print("Transaction Successful")
                
        case 5:
            print(f"Your balance is: {obj1.get_balance()}")
            
        case 6:
            bank.show_accounts()
            
        case 7:
            print("--- Personal Transaction History ---")
            obj1.transation_history()
            
        case 8:
            print("Thank you for using the banking system!")
            break        
        case _:
            print("Invalid Option. Please choose 1-8.")
