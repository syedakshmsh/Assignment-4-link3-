import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

# Generate a random number between 1 and 10
secret_number = random.randint(1,10)
print("select a secret number you guess it")

while True:
    try:
        guess = int(input("enter a guess number:"))
        if guess > secret_number:
            print("guess so high !Try again")
        if guess < secret_number:
            print("guess so low !Try again")
        else:
            print("congratulation you guess a secret number")
    except ValueError:
        print("Invalid input please enter a number between 1 to 10 ")
        

