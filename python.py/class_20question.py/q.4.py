class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created successfully.")
        else:
            print("Account already exists. Please choose a different account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None  # Added a return statement for consistency

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} into account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                print(f"Withdrew ${amount} from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

# Example usage:
bank = Bank()

bank.create_account("12345", 1000)
bank.deposit("12345", 500)
balance = bank.check_balance("12345")
if balance is not None:
    print(f"Account Balance: ${balance}")

bank.withdraw("12345", 200)
balance = bank.check_balance("12345")
if balance is not None:
    print(f"Account Balance: ${balance}")
