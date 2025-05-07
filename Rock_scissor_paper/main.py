import random

print("Welcome to play Rock ,Scissor, paper:")

choices = ["Rock","Scissor","Paper"]
user_score = comuter_score = 0
print("Lets play")


while True:
    user_input = (input("Type rock,paper,scissor or Q to Quit")).lower()
    
    if user_input == "Q":
        print(f"Final score - you : {user_score} ,computer : {comuter_score}")
        print("Thank you Playing:")
        break
    if user_input not in choices:
        print("Invalid input please try again")
        continue
    computer_choice = random.choice(choices)
    print(f"computer choice {computer_choice}")
    if user_input == computer_choice:
        print("its to tie:")
    elif (user_input == "rock" and computer_choice == "scissor") or \
         (user_input == "scissor" and computer_choice == "paper") or \
         (user_input == "paper" and computer_choice == "rock") or \
         print("you Win"):
         user_score += 1
    else:
        print("computer wins!")
        comuter_score += 1
    print(f"current score - you {user_score}, computer: {comuter_score}")

         
         
         