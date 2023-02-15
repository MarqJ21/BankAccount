class BankAccount:
    int_rate = .1
    balance = 0
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.rate)
        else:
            print("Account is negative")
        return self

# John = BankAccount(.1,300)
# Matt = BankAccount(.1,400)

# John.deposit(30).deposit(70).deposit(40).withdraw(25).yield_intrest().display_account_info()

# Matt.deposit(80).deposit(50).withdraw(40).withdraw(5).withdraw(10).withdraw(10).yield_intrest().display_account_info()



