import pdb
from budget import Budget

budgetc = int(input("What is your total budget for clothing: "))
budgete = int(input("What is your total budget for entertainment: "))
budgetf = int(input("What is your total budget for food: "))

food = Budget(budgetf)
file1 = open("food.txt", "w")
file1.write(str(food.balance))
file1.close()
clothing = Budget(budgetc)
file2 = open("clothing.txt", "w")
file2.write(str(clothing.balance))
file2.close()
entertainment = Budget (budgete)
file3 = open("entertainment.txt", "w")
file3.write(str(entertainment.balance))
file3.close()

#app2.py replace lines 3-5 with values that already exist to be saved 

#Need to create function for either creating new budget or using existing budget

#If enters invalid amount to display error message

loop = True

while loop:
    transfer_type = input("What would you like to do? \n(T) Transfer between budgets \n(D) Deposit funds \n(W) Withdraw funds \n(B)Display Balance \n(E) Exit\n").upper()
    if transfer_type == "T":
        transfer_source = input("Where would you like to move the funds from?(c/e/f) ").lower()
        amount = int(input("What is the amount? "))
        transfer_destination = input("Where would you like to transfer the money to? (c/e/f) ").lower()
        if transfer_source == "c":
            if transfer_destination == "e":
                clothing.balance = clothing.balance - clothing.withdraw(amount)
                entertainment.balance = entertainment.balance + entertainment.deposit(amount)
                print(f"New total budget for clothing is {clothing.balance}")
                print(f"New total budget for entertainment is {entertainment.balance}")
                file2 = open("clothing.txt", "w")
                file2.write(str(clothing.balance))
                file2.close()
                file3 = open("entertainment.txt", "w")
                file3.write(str(entertainment.balance))
                file3.close()
            elif transfer_destination == "f":
                clothing.balance = clothing.balance - clothing.withdraw(amount)
                food.balance = food.balance + food.deposit(amount)
                print(f"New total budget for clothing is {clothing.balance}")
                print(f"New total budget for food is {food.balance}")
                file1 = open("food.txt", "w")
                file1.write(str(food.balance))
                file1.close()
                file2 = open("clothing.txt", "w")
                file2.write(str(clothing.balance))
                file2.close()
            else:
                print("Please input valid destination")
        elif transfer_source == "e":
            if transfer_destination == "c":
                entertainment.balance = entertainment.balance - entertainment.withdraw(amount)
                clothing.balance = clothing.balance + clothing.deposit(amount)
                print(f"New total budget for entertainment is {entertainment.balance}")
                print(f"New total budget for clothing is {clothing.balance}")
                file2 = open("clothing.txt", "w")
                file2.write(str(clothing.balance))
                file2.close()
                file3 = open("entertainment.txt", "w")
                file3.write(str(entertainment.balance))
                file3.close()
            elif transfer_destination == "f":
                entertainment.balance = entertainment.balance - entertainment.withdraw(amount)
                food.balance = food.balance + food.deposit(amount)
                print(f"New total budget for entertainment is {entertainment.balance}")
                print(f"New total budget for food is {food.balance}")
                file1 = open("food.txt", "w")
                file1.write(str(food.balance))
                file1.close()
                file3 = open("entertainment.txt", "w")
                file3.write(str(entertainment.balance))
                file3.close()
            else:
                print("Please input valid destination")
        elif transfer_source == "f":
            if transfer_destination == "c":
                food.balance = food.balance - food.withdraw(amount)
                clothing.balance = clothing.balance + clothing.deposit(amount)
                print(f"New total budget for food is {food.balance}")
                print(f"New total budget for clothing is {clothing.balance}")
                file1 = open("food.txt", "w")
                file1.write(str(food.balance))
                file1.close()
                file2 = open("clothing.txt", "w")
                file2.write(str(clothing.balance))
                file2.close()
            elif transfer_destination == "e":
                food.balance = food.balance - food.withdraw(amount)
                entertainment.balance = entertainment.balance + entertainment.deposit(amount)
                print(f"New total budget for food is {food.balance}")
                print(f"New total budget for entertainment is {entertainment.balance}")
                file1 = open("food.txt", "w")
                file1.write(str(food.balance))
                file1.close()
                file3 = open("entertainment.txt", "w")
                file3.write(str(entertainment.balance))
                file3.close()
            else:
                print("Please input valid destination")
        else:
            print("Please input valid source")
    elif transfer_type =="W":
        transfer_source = input("Where would you like to move the funds from?(c/e/f) ").lower()
        amount = int(input("What is the amount? "))
        if transfer_source == "c":
            clothing.balance = clothing.balance - clothing.withdraw(amount)
            print(f"You have £{clothing.balance} remaining in your clothing budget.") 
            file2 = open("clothing.txt", "w")
            file2.write(str(clothing.balance))
            file2.close()
        elif transfer_source == "e":
            entertainment.balance = entertainment.balance - entertainment.withdraw(amount)
            print(f"You have £{entertainment.balance} remaining in your entertainment budget.")
            file3 = open("entertainment.txt", "w")
            file3.write(str(entertainment.balance))
            file3.close()
        elif transfer_source == "f":
            food.balance = food.balance - food.withdraw(amount)
            print(f"You have £{food.balance} remaining in your entertainment budget.") 
            file1 = open("food.txt", "w")
            file1.write(str(food.balance))
            file1.close()
        else:
            print("Please input valid source")
    elif transfer_type == "D":
        transfer_source = input("Where would you like to deposit the funds?(c/e/f) ").lower()
        amount = int(input("What is the amount? "))
        if transfer_source == "c":
            clothing.balance = clothing.balance + clothing.deposit(amount)
            print(f"You now have £{clothing.balance} in your clothing budget.") 
            file2 = open("clothing.txt", "w")
            file2.write(str(clothing.balance))
            file2.close()
        elif transfer_source == "e":
            entertainment.balance = entertainment.balance + entertainment.deposit(amount)
            print(f"You now have £{entertainment.balance} in your entertainment budget.") 
            file3 = open("entertainment.txt", "w")
            file3.write(str(entertainment.balance))
            file3.close()
        elif transfer_source =="f":
            food.balance = food.balance + food.deposit(amount)
            print(f"You now have £{food.balance} in your food budget.") 
            file1 = open("food.txt", "w")
            file1.write(str(food.balance))
            file1.close()
        else:
            print("Please input valid destination")
    elif transfer_type == "B":
        transfer_source = input("Which balance would you like to display? (c/e/f)? ").lower()
        if transfer_source == "f":
            print(f"Your food budget is {food.balance}")
        elif transfer_source == "c":
            print(f"Your clothing budget is {clothing.balance}")
        elif transfer_source == "e":
            print(f"Your entertainment budget is {entertainment.balance}")
        else:
            print("Please input valid budget to view")
    elif transfer_type == "E":
        loop = False
    else:
        print("\nPlease enter valid command\n")



