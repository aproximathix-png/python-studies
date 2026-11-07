#  comments
import random

secret = random.randint(1, 10)

print("Choose a number")
guess = int(input("Your guess: "))
attemp = 0
while guess != secret:

    if guess > secret:
        print("Too high! Try again.")

    elif guess < secret:
        print("Too low! Try again.")
    if attemp > 5 :
         break

    guess = int(input("Your guess: "))
    attemp+= 1
    
    
if attemp < 5 and guess == secret:
         print("You won! and you took" , attemp ,"attemp")



    

    
      
       

