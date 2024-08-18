import random
items = ["rock","paper","scissors"]
def get_computer_choice():
    return random.choice(items)

def get_user_choice():
    while True:
        user_input = input("rock,paper,scissors?").lower()
        if user_input in items:
            return user_input
        print("invalid")


def winner(user_choice,computer_choice):
    if user_choice== computer_choice:
        print("same item")
    elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "scissors" and computer_choice == "paper") or (
            user_choice == "paper" and computer_choice == "rock"):
        print("You win against to computer")
    else:
        print("computer wins")
        
                        

def start_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner(user_choice, computer_choice)
        
        query = input("Do you want to play again? (yes/no): ").lower()
        if query != "yes":
            break
start_game()       