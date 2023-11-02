# Making a number gussing game 
import random
a = random.randint(1,100)
attempt = 1
while True:
    user_input = int(input("Guess the number to win : "))
    if user_input < a:
        print("You , Guessed very low !")
    elif user_input > a:
        print("You Guessed Very High !")
    elif user_input == a :
        print("Congratualaion , You Won ")
        break
    else :
        print("Invalid Input , Please enter the number between 1 to 100")
    attempt += 1
print("You Won in ",attempt,"attempt")