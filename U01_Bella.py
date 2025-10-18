import random

choices = ["rock", "paper", "scissors"]
choices1 = ["rock", "paper", "scissors","gun","AK-47"]
def rps (player,computer):
    if player==computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper") or \
            (player=="AK-47")or \
            (player=="gun"):
        return "player won"
    else:
        return "computer won"


pcscore=0
plscore=0
print("we are playing rock paper scissors Bo3")

for round in range (1,4):


    player=input("choose:")
    if player=="gun" or player=="AK-47":
        print("Nice one :)")
    if player not in choices1: ##nie je to while loop lebo mi to prislo vtipné
        player= input("Invalid choice, choose again:")
        if player not in choices1:
            player = input("Invalid choice, choose again:")
            if player not in choices1:
                player = input("INVALID CHOICE, choose again:")
                if player not in choices1:
                    player = input("BRO ITS INVALID, CHOOSE AGAIN:")
                    if player not in choices1:
                        player = input("PLEASE, CHOOSE AGAIN:")
                        if player not in choices1:
                            player = input("This is painfull, choose again:")
                            if player not in choices1:
                                player = input("Every time you do this it hurts more and more,")
                                if player not in choices1:
                                    player = input("You found an easter egg, gun, was it worth it?")



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