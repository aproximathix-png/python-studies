
def deposit_money(balance):
    deposit = int(input("Enter the amount to deposit: "))
    if deposit <= 0:
        print("You can't deposit negative money")
    else:
        balance += deposit
    return balance 

def withdraw_money(balance):
    withdrow = int(input("Enter the amount to withdraw: "))
    if withdrow > balance:
        print("You don't have enough money")
    elif withdrow <= 0:
            print("You can't withdraw negative money")
    else:
            balance -= withdrow
            print("Your new balance is: ", balance)
            return balance

            


balance = 1000
restart = True
while restart:

    print("##### Welcome to the Bank #####")
    print("1. check balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. exit")
    answer = int(input("You chose: "))


    if answer == 1:
     print("Your balance is: ", balance)



    if answer == 2:
        balance = deposit_money(balance)


    if answer == 3:
        balance = withdraw_money(balance)

    if answer == 4:
        print("Thank you for using our bank")
        break

    elif answer > 4 or answer < 1:
        print("error you put the wrong number")


  

