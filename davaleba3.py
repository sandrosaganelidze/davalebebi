from random import choice
 
choice_list = ["rock", "scissors", "paper"]
computer_choice = choice(choice_list)
 
human_choice = input("Enter one of the following: rock / scissors / paper ").lower()
 
if human_choice in choice_list:
    if human_choice == computer_choice:
        print("Draw!")
    elif (human_choice == "rock" and computer_choice == "scissors") or (human_choice == "scissors" and computer_choice == "paper") or (human_choice == "paper" and computer_choice == "rock"):
        print("Human Wins!")
    else:
        print("Computer Wins!")