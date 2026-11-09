import json
expenses = []
try:
    with open('data.json', 'r') as r:
        expenses = json.load(r)
except FileNotFoundError:
    expenses = []


restart = True
while restart:
    print("Welcome to the Expense Tracker!")
    print("what do you want to do?")
    print("1. Add an expense")
    print("2. View expenses")
    print (" 3 delete an expense")
    print("4 total spending")
    print("5 exit")
    answer = input("Enter your choice (1-5): ")
    while answer not in ["1", "2", "3", "4", "5"]:
        print("Invalid input. Please enter a number between 1 and 5.")
        answer = input("Enter your choice (1-5): ")

    if answer == "1":
        print("Enter the expense details:")
        validation1 = False
        while validation1 == False:
                name = input("Name: ")
                name = name.strip()
                if name == "":
                    print("Name can't be empty")
                    validation1 = False
                else:
                    validation1 = True
        validation = False
        while validation == False:
            try:
                amount = float(input("Amount: "))
                price = float(input("Price: ")) 
                if amount < 0 or price < 0:
                    print("Amount and price must be non-negative(zero is allowed). Please try again.")
                    validation = False  
                else:
                    validation = True  
            except ValueError:
                print("The value has wrong format")
        expense = {"name": name, "amount": amount, "price": price}
        expenses.append(expense)
     

    if answer == "2":
        if expenses == []:
            print("No expenses found.")
        for index, value in enumerate(expenses):
            print(f'{index}: {value}')


    if answer == "3":
        
        if  expenses == []:
            print("No expenses found.")  
        else:         
            print("Enter the index of the expense to delete:")
        
            index = (input())
            while not index.isdigit() or int(index) >= len(expenses):
                print("Invalid input. Please enter a valid index.")
                index = input()
            expenses.pop(int(index))
            print("Expense removed successfully")
 
    if answer == "4":
        total_spending = sum(expense["amount"] * expense["price"] for expense in expenses)
        print(f"Total spending: {total_spending}")

    with open("data.json", "w") as f:
        json.dump(expenses, f)

    if answer == "5":
        restart = False
        print("Exiting the Expense Tracker. Goodbye!")