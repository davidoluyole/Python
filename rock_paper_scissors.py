#rock/paper/scissors
#rock / paper=paper
#rock / scissors=rock
#paper / scissors=scissors

import random

guess = input("Enter rock or paper or scissors: ")
computer_choice = ["rock", "paper", "scissors"]
computer = random.choice(computer_choice)
count = 0

while count < 100:

    if computer == guess:
        print("No winner")

    elif guess == "rock":
        if computer == "scissors":
            print("you won, rock smashes scissors")
        elif computer == "paper":
            print("Computer wins, paper covers rock")
    elif guess == "paper":
        if computer == "rock":
            print("you won, paper covers rock")
        elif computer == "scissors":
            print("computer wins, Scissors cuts paper")
    elif guess == "scissors":
        if computer == "paper":
            print("you won, scissors cuts paper")
        elif computer == "rock":
            print("computer wins, rock smashes scissors")
    elif guess == "1":
        print("thanks for playing")
        break

    guess = input("Enter rock or paper or scissors or enter 1 to end: ")
    count +=1

