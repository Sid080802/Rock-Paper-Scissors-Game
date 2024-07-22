import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower().strip()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer Picked ", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You Wins ")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You Wins ")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Wins ")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("No one win")
        continue
    else:
        print("Computer Wins")
        computer_wins += 1
        continue

print("You won", user_wins, "times. ")
print("The Computer won", computer_wins, "times. ")
print("Good Bye! ")
