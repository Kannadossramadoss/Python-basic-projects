# import random module
import random

# Initializing result variables.
user_wins = 0
computer_wins = 0

# store possible values in a list.
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # Quit the script if user entered Q
    if user_input == "q":
        break

    # validate the user input.
    if user_input not in options:
        print("Enter a valid input: ")
        continue
    random_number = random.randint(0, 2)

    # rock: 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Game ends!")
