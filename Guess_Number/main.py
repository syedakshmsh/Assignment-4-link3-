import random

print("Welcom to the number guessing game")


low = 1
high = 10 

print("Think a Number Computer guess it the number")


if low <= high:
    guess = random.randint(low,high)
    print("Computer guess a number:",guess)

while True:
    feedback = input("Is the guess too high (H), too Low (L),or correct too (C):").strip().upper()

    if feedback == 'C':
        print("yay! The Computer guess:",guess)
        break
    elif feedback == "H":
        high = guess -1
        guess = random.randint(low,high)
        print("yay! The Computer guess:",guess)
    elif feedback == "L":
        high = guess + 1
        guess = random.randint(low,high)
        print("yay! The Computer guess:",guess)

    else:
        print("Invalid Input. Please enter a H,C,L")
if low > high:
    print("The number in not in the range:Please try again")




