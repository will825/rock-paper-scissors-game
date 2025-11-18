# Rock_Paper_Sissors_Game.py


import random
import time

choices = ["rock", "paper", "scissors"]

player_round_taunts = [
    "Nice one.",
    "You're getting good at this.",
    "Alright, alright, calm down.",
    "That had to hurt the computer's feelings."
]

computer_round_taunts = [
    "Too easy.",
    "You call that a move?",
    "Try again, human.",
    "That was rough..."
]

player_match_taunts = [
    "You totally smoked the computer.",
    "You owned that match.",
    "Computer never stood a chance."
]

computer_match_taunts = [
    "The computer dominated you.",
    "Ouch. That was not your best work.",
    "Computer says: better luck next time."
]

print("Welcome to Rock, Paper, Scissors!")

while True:
    player_wins = 0
    computer_wins = 0

    print("\nNew match! First to 2 wins.\n")

    while player_wins < 2 and computer_wins < 2:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("Not a valid choice. Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        time.sleep(0.3)

        # Determine round winner
        if (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round.")
            player_wins += 1
            print(random.choice(player_round_taunts))

        elif player_choice == computer_choice:
            print("It's a tie this round.")

        else:
            print("Computer wins this round.")
            computer_wins += 1
            print(random.choice(computer_round_taunts))

        print(f"Score -> You: {player_wins}, Computer: {computer_wins}\n")

    # End of match
    print("==============================")
    print("Final Score:")
    print(f"You: {player_wins}  |  Computer: {computer_wins}")

    if player_wins > computer_wins:
        print("Congratulations! You won the match.")
        print(random.choice(player_match_taunts))
    else:
        print("The computer won the match.")
        print(random.choice(computer_match_taunts))

    print("==============================")

    # Replay menu
    play_again = input("Do you want to play another match? (yes/no): ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing!")
        break
