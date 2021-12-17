from budget2 import Budget


#Create budget category and how much in each category or ?upload from file already created




var1 = input("Enter amount you would like to budget to this category: £")
var2 = input("What would you like to? \n(T) Transfer between budgets \n(D) Deposit funds \n(W) Withdraw funds \n(B)Display Balance \n(E) Exit\n").upper()


for var2 in ["T", "D", "W", "B", "E"]:
    break
else:
    var2 = input("Please input valid choice (T/D/W/B/E): ")


food = Budget(var1, var2)
clothing = Budget(var1, var2)