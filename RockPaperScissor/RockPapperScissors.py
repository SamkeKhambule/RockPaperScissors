import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds (e.g., 3, 5, 7): "))

    while player_score < rounds // 2 + 1 and computer_score < rounds // 2 + 1:
        print("\nRock, Paper, Scissors Game!")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            player_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("You lose this round!")
        else:
            print("It's a tie!")
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You won the series!")
    else:
        print("Sorry, you lost the series. Better luck next time!")

play_game()
