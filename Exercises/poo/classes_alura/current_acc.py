class Account:
    def __init__(self, number:int, name_cur:str, balance=0):
        self.number = number
        self.name_cur = name_cur.capitalize().strip()
        self.balance  = balance

    def changeName(self, newname):
        self.name_cur = newname
    
    def deposit(self, value:float):
        self.balance += value
        print(f"Value ${value} deposited.")

    def withdraw(self, value:float):
        if (value > self.value):
            print(f"There is no value ${value} on this account.")
        else:
            self.balance -= value

    def showBalance(self) -> float:
        return self.balance

account = Account(8326, "Carlos", 43)
print(account.showBalance())
account.deposit(8)
print(account.showBalance())
