import random

# List of valid options
choices = ["rock", "paper", "scissors"]

def rps(player, computer):
    """Determine the winner of a Rock-Paper-Scissors round.

        player (str): The player's choice ("rock", "paper", or "scissors").
        computer (str): The computer's choice ("rock", "paper", or "scissors").

    Returns:
        str: "player won" if the player wins,
             "computer won" if the computer wins,
             "draw" if both choose the same.
    """
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player won"
    else:
        return "computer won"


# Initialize scores
pcscore = 0
plscore = 0
print("We are playing Rock-Paper-Scissors Bo3")

# Loop for 3 rounds
for round in range(1, 4):

    # Ask player for valid input
    while True:
        player = input("Choose (rock/paper/scissors): ").lower()
        if player in choices:
            break
        print("Invalid choice, please choose again.")

    # Computer randomly chooses
    computer = random.choice(choices)
    print("The computer chose:", computer)

    # Determine round result
    result = rps(player, computer)

    # Update scores and print result
    if result == "player won":
        print("player won")
        plscore += 1
    elif result == "computer won":
        print("computer won")
        pcscore += 1
    else:
        print("draw")

    # Show current score
    print("Score is: pc:", pcscore, "player:", plscore)

# Final results
print("FINAL score is: pc:", pcscore, "player:", plscore)
if pcscore > plscore:
    print("COMPUTER WINS")
elif plscore > pcscore:
    print("PLAYER WON")
else:
    print("DRAW")
