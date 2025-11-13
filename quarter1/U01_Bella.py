import random  # To allow computer to make random choices

# List of valid options
choices = ["rock", "paper", "scissors"]

# Function to determine winner of a single round
def rps(player, computer):
    if player == computer:
        return "draw"  # Same choice -> draw
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player won"  # Player beats computer
    else:
        return "computer won"  # Computer beats player

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
