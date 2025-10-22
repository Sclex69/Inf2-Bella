import random

choices = ["rock", "paper", "scissors"]

def rps (player,computer):
    if player==computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        return "player won"
    else:
        return "computer won"


pcscore=0
plscore=0
print("we are playing rock paper scissors Bo3")

for round in range (1,4):


    while True:
        player = input("Choose (rock/paper/scissors/): ").lower()
        if player in choices:
            break
        print("Invalid choice, please choose again.")


    computer= random.choice(choices)
    print("The computer chose:", computer)

    result=rps(player,computer)

    if result == "player won":
        print("player won")
        plscore+=1
    elif result == "computer won":
        print("computer won")
        pcscore+=1
    else:
        print("draw")


    print("score is: pc: ", pcscore, " player: ",plscore)
print("FINAL score is: pc: ", pcscore, " player: ",plscore)
if pcscore>plscore:
    print("COMPUTER WINS")
elif plscore>pcscore:
    print("PLAYER WON")
else:
    print("DRAW")