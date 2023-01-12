from Classes import*
from Text import*
from Funktioner import*
from exploring import*

list = [1,2,3,4,5]


def initiate_combat():

    animate_typing("You encountered a (baserat på vart man är i spelet) ") 

def attack():
    while True:
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3:
            animate_typing("\nYou hit the target.")
        else:
            animate_typing("\nYou missed.")

def block():
    while True:
        outcome=random.choice(list)
        if outcome==1 or 2 or 3
            animate_typing("\nSuccessfully blocked!")
        else:
            animate_typing("\nyou took ... damage")

    



def choices():
    choice= """What will you do now?"""
    animate_typing(choice)
    x=int(input("")) 
    if x==1: 
        attack
    if x==2:
        block
choices()

        





