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

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(.01, 0)

    def make_deposit(self, amount):
        self.account.balance += amount

    def make_withdraw(self, amount):
        self.account.balance -= amount
    
    def display_user_balance(self):
        print(self.account.balance)

def display_info(self):
    print(self.first, self.last, self.email, self.age, self.is_rewards_member, self.gold_card_points)

def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points = 200

def spend_points(self, amount):
    self.gold_card_points = self.gold_card_points - amount

marques = User("Marques", "Johnson",  "mfj@gmai.com", "20")
justin = User("Justin", "Henderson", "jhendo@msn.com", "19")

enroll(marques)

spend_points(marques, 50)

enroll(justin)

spend_points(justin, 80)

display_info(marques)
display_info(justin)






