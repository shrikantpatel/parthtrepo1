#to get the computers choices we have to import random
import random
while True:
#we have to take an input from the user
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    #we must now make the computer choose from the choices
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print("You chose {}, computer chose {}.".format(user_choice, computer_choice))

    if user_choice == computer_choice:
        print("Both players selected {}." .format(user_choice))
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose, paper covers rock!")
        else:
            print("You win, rock smashes scissors!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win, paper covers rock!")
        else :
            print("You lose, scissors cut paper!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win, scissors cut paper!")
        else:
            print("You lose, rock smashes scissors!")
        
    next_calculation = input("Continue Calculating? (yes/no): ")
    if next_calculation == "no":
            break
else:
    print("Invalid Input")