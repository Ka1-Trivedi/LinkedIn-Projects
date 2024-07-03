#Decoration part
# 🦯 stick
from pyfiglet import Figlet
import random
import sys

#FontWork for given string 
def ascii_art(str):
    figlet = Figlet()
    figlet.setFont(font="big")
    print(figlet.renderText(str))

#Taking Input From User
def get_input():
    # A=input("Name of Player A: ")
    # B=input("Name of Player B: ")
    names=list(map(str.strip,input("Enter the name of two players(Ex. PlayerA and PlayerB): ").split("and")))
    random.shuffle(names)
    A,B=names
    print("You have a choice here:")
    try:
        choice=int(input("Enter 1 :If you want to select number of stick in heap.\nEnter 2 :If you want number of stick to be random.\n"))
        if choice==1:
            n=int(input("Enter the number of stick in heap: "))
        elif choice==2:
            n=random.randint(1,31)
    except ValueError:
        sys.exit("Invalid Input:")
    print("*"*50)
    print(f"Let us consider a game where there is initially a heap of n-sticks.\nPlayers {A} and {B} move alternately, and player {A} begins.\nOn each move, the player has to remove 1, 2, or 3 sticks from the heap,\nand the player who removes the last stick wins the game.")
    print("*"*50)
    return A,B,n

#Pridicting Winner based on starting turn and number of stick if both player play Optimaly
def get_winner(A,B,n):
    if n%4==0:
        return B
    else:
        return A

#Begins the game between two minds
def play_game(A,B,n):
    print("The perosn whoes name will apper have to select 1,2 or 3 sticks (🦯)")
    print("Total Sticks:","🦯"*n)
    while n>0:
        try:
            tempA=int(input(f"{A}: "))
            if(tempA==1 or tempA==2 or tempA==3) and n-tempA>=0:
                n-=tempA
                if(n==0):
                    return A
                else:
                    print("Remaining sticks:","🦯"*n)
                    ascii_art(f"Sticks = {n}")
            else:
                print(f"Wrong Input!!\n{A}'s turn has been skipped.")
            tempB=int(input(f"{B}: "))
            if(tempB==1 or tempB==2 or tempB==3) and n-tempB>=0:
                n-=tempB
                if(n==0):
                    return B
                else:
                    print("Remaining sticks:","🦯"*n)
                    ascii_art(f"Sticks = {n}")
            else:
                print(f"Wrong Input!!\n{B}'s turn has been skipped.")
        except TypeError:
            pass
        except ValueError:
            pass
            
#Handling the Functional calling and Printing Winner
def main():
    A,B,n=get_input()
    Optimum_winner=get_winner(A,B,n)
    ascii_art(f"Stick = {n}")
    winner=play_game(A,B,n)
    ascii_art(f"{winner} is the Winner")
    if Optimum_winner != winner:
        print("*"*80)
        print("If the game was played optimaly the winner would be :")
        ascii_art(Optimum_winner)
if __name__=="__main__":
    main()
