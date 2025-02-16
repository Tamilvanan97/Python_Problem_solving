import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    
    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in choices :
            print('invalid input, Choose value between (rock, paper, scissors)')
        else :
            if user == computer:
                print("It's a tie!")
            elif (user == "rock" and computer == "scissors") or \
                (user == "paper" and computer == "rock") or \
                (user == "scissors" and computer == "paper"):
                print("You win!")
                print("Computer chose:", computer)
                break
            else:
                print("You lose!")
                print("Computer chose:", computer)

play_game()
