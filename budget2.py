#constructor, will have encapsulation within

class Budget():
    def __init__(self, balance=0, category="None"):
        self.balance = balance
        self.category = category


    def __repr__(self):
        return f"This is the {self.category} budget"

#methods
    def deposit(self, amount):
        if amount <0:
            return "Invalid amount entered"
        else:
            self.balance =+ amount
            return f"Current balance is £{self.balance}"

    def withdraw(self, amount):
        self.balance =- amount
        return f"Current balance is £{self.balance}"

    def get_balance(self):
        return f"This is your current balance: £{self.balance}"

    def transfer(self, amount, category):
        self.withdraw (amount, f"Transfer to {category.category}")
        category.deposit(amount, f"Tranfer from({self.category}")