class Budget():
    def __init__(self, balance):
        self.balance = balance
    
    def __rpr__(self):
        return f"Total budget = {self.balance}"

    def deposit(self, amount):
        self.balance =+ amount
        return amount
         

    def withdraw(self, amount):
        self.balance =- amount 
        return amount