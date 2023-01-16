from Classes import*
from Text import*
from Funktioner import*
from exploring import*

list = [1,2,3,4,5,6]

def attack():
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3:
            animate_typing("\nYou hit the target.")
        else:
            animate_typing("\nYou missed.")

def block():
        outcome=random.choice(list)
        if outcome==1 or 2 or 3:
            animate_typing("\nSuccessfully blocked!")
        else:
            animate_typing("\nyou took ... damage")

def choices():
    combat_options = ("""
What will you do now?

1 - Attack
2 - Block

Your choice --> """)
    while True:
        animate_typing(combat_options)
        x=int(input("")) 
        if x==1: 
            attack()
        elif x==2:
            block()

        
def initiate_combat():
    choices()

initiate_combat()