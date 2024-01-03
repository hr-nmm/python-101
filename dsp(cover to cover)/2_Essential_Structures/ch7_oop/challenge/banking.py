# Challenge: Create a simple banking system with two classes: Account and Bank.Your implementation should allow for the creation of accounts, deposits, withdrawals, and retrieval of account balances within the context of the bank.


class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(
            f"ACCOUNT:{self.account_number} => Your last deposit was Rs.{amount} and your current balance is Rs.{self.balance}"
        )

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(
                f"ACCOUNT:{self.account_number} => Withdrawl unsuccessful!! REASON: Insufficient funds. Balance : Rs.{self.balance}."
            )
            return
        print(
            f"ACCOUNT:{self.account_number} => Your last withraw was Rs.{amount} and your current balance is Rs.{self.balance}"
        )

    def getBalance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number):
        new_account = Account(account_number)
        self.accounts[account_number] = new_account
        print(f"ACCOUNT:{account_number} => created successfully.")

    def get_account(self, account_number):
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        acc_obj = self.get_account(account_number)
        acc_obj.deposit(amount)

    def withdraw(self, account_number, amount):
        acc_obj = self.get_account(account_number)
        acc_obj.withdraw(amount)

    def get_balance(self, account_number):
        return self.get_account(account_number).getBalance()


## driver
bank = Bank()

bank.add_account(10001)
bank.add_account(10002)

bank.deposit(10001, 500)
bank.withdraw(10001, 200)
print("Account 10001 Balance:", bank.get_balance(10001))

bank.deposit(10002, 1000)
bank.withdraw(10002, 1200)  # This withdrawal will fail due to insufficient funds
print("Account 10002 Balance:", bank.get_balance(10002))

## o/p:
# ACCOUNT:10001 => Your last deposit was Rs.500 and your current balance is Rs.500
# ACCOUNT:10001 => Your last withraw was Rs.200 and your current balance is Rs.300
# Account 10001 Balance: 300
# ACCOUNT:10002 => Your last deposit was Rs.1000 and your current balance is Rs.1000
# ACCOUNT:10002 => Withdrawl unsuccessful!! REASON: Insufficient funds. Balance : Rs.1000.
# Account 10002 Balance: 1000
