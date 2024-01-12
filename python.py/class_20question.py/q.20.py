class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

class Transaction:
    @staticmethod
    def withdraw(account, amount):
        if amount > 0 and account.balance >= amount:
            account.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${account.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    @staticmethod
    def check_balance(account):
        print(f"Current balance for account {account.account_number}: ${account.balance}")

class User:
    def __init__(self, username, accounts):
        self.username = username
        self.accounts = accounts

    def verify_pin(self, account_number, entered_pin):
        # Verify PIN for the specified account
        for account in self.accounts:
            if account.account_number == account_number and account.pin == entered_pin:
                return True
        return False

    def perform_transaction(self, account_number, entered_pin, transaction_type, amount=None):
        # Perform the specified transaction if PIN is verified
        for account in self.accounts:
            if account.account_number == account_number and self.verify_pin(account_number, entered_pin):
                if transaction_type == "withdraw":
                    Transaction.withdraw(account, amount)
                elif transaction_type == "check_balance":
                    Transaction.check_balance(account)
                else:
                    print("Invalid transaction type.")
                return

        print("Invalid account number or PIN.")

# Example usage:
# Create accounts, users, and perform transactions
account1 = Account("123456789", "1234", 1000)
account2 = Account("987654321", "5678", 500)

user1 = User("Alice", [account1])
user2 = User("Bob", [account2])

# Perform transactions
user1.perform_transaction("123456789", "1234", "withdraw", 200)
user1.perform_transaction("123456789", "1234", "check_balance")

user2.perform_transaction("987654321", "5678", "withdraw", 600)
user2.perform_transaction("987654321", "5678", "check_balance")
