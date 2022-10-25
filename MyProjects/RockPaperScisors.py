#this is a Rock Paper scissors game

# Rules 
#1. Rock wins over scissors and loose to paper 
#2. Paper wins over rock and loose to scissors
#3. Scissors wins over paper and loose to rock

import random

comp=random.randint(1,3)
if comp==1:
    comp="r"
elif comp==2:
    comp="p"
else:
    comp="s"

Player = input("Choose Rock(r) paper(p) or scissors(s)")
print("Computer choose : ",comp)

def youWin(comp,player):
    if comp==player:
        return None
    elif comp=="r":
        if player=="p":
            return True
        elif player=="s":
            return False
    elif comp=="p":
        if player =="s":
            return True
        elif player=="r":
            return False
    elif comp =="s":
        if player=="r":
            return True
        elif player =="p":
            return False
if youWin(comp,Player) == True:
    print("You Win")
elif youWin(comp,Player)==False:
    print("You loose")
else:
    print("Tie")