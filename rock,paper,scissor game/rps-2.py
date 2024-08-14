import sys , random 
from enum import Enum


class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    
while True:
    game=int(input("How many games you want to play:"))
    for gameplay in range(game):
        print("")
        print(f"Game:{gameplay+1}")
        playerchoice=input("Enter... \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n\nEnter your choice:")
        player=int(playerchoice)
        if player<1 or player>3:
            sys.exit("Enter valid choice")
            
        computerchoice=random.choice("123")
        computer=int(computerchoice)
            
        print("\nYou chose "+str(RPS(player)).replace("RPS.","")+".\n")
        print("Computer chose "+str(RPS(computer)).replace("RPS.","")+".\n")
            
        if computer==player:
            print("😧 Tie Game")
        elif player==1 and computer==2:
            print("🖥️ Computer Won")
        elif player==1 and computer==3:
            print("🎉 You Won")
        elif player==2 and computer==1:
            print("🎉 You Won")
        elif player==2 and computer==3:
            print("🖥️ Computer Won")
        elif player==3 and computer==2:
            print("🎉 You Won")
        else:
            print("🖥️ Computer Won")
            
    
        
    while True:
        count=input("Do you want to continue playing Enter y or n:\n").lower()
        if count in ['y','n']:
            break
        else:
            print("Enter valid input")
        
    if count=='y':
        continue
    else:
        print("Thank you for playing!")
        break