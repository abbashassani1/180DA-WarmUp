
import random

#initialize scores
scores = {'wins': 0, 'losses': 0, 'ties': 0}

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter rock, paper, or scissors: ")
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        scores['ties'] += 1
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        scores['wins'] += 1
        return "You win!"
    else:
        scores['losses'] += 1
        return "You lose!"

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    print(f"Score: {scores['wins']} Wins, {scores['losses']} Losses, {scores['ties']} Ties")

if __name__ == "__main__":
    while True:  # Loop to keep the game running
        play()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break
