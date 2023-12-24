# Class - Blueprint of an object & OOP
## A Simple bank account:
class Account:
    owner : str
    balance : float
    passbook : dict
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        self.passbook = {"balance":balance,"credit":0.0,"debit":0.0}

    def __repr__(self) -> str:
        return f'Account({self.owner!r}, {self.balance!r}, {self.passbook!r})'

    def deposit(self, amount) -> dict:
        self.balance += amount
        self.passbook.update({"balance":self.balance,"credit":amount,"debit":0.0})
        return self.passbook

    def withdraw(self, amount) -> dict:
        self.balance -= amount
        self.passbook.update({"balance":self.balance,"credit":0.0,"debit":amount})
        return self.passbook

    def inquiry(self) -> float:
        return self.balance
    

x = Account("Himanshu",16_000)
print(x)
print(x.deposit(8_000.0))
print(x.withdraw(2500))
print(x.inquiry())
print(x)
print(vars(x))
    