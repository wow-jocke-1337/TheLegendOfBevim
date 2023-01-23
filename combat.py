from Text import*
from Funktioner import*

list = [1,2,3,4,5,6]

def attack():
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3 or 4:
            animate_typing("\nYou hit the target!")
            damage()
        else:
            animate_typing("\nYou missed.")

def block():
        outcome=random.choice(list)
        if outcome==1 or outcome==2 or outcome==3:
            animate_typing("\nSuccessfully blocked!")
        else:
            animate_typing("\nyou failed to block and took damage!"  + {Player.STR} *0.25)


def Exit_Combat(): 
        outcome= random.choice(list)
        if outcome== 1 or 2:
            animate_typing("\nSuccess! You ran away")
        else:
            animate_typing("\You Failed to Run Away!")




def choices():
    combat_options = ("""
What will you do now?

1 - Attack
2 - Block
3 - Check inventory
4 - Run Away

Your choice --> """)
    while True:
        animate_typing(combat_options)
        x=int(input("")) 
        if x==1: 
            attack()
            break
        elif x==2:
            block()
            break

def damage():
    while True:
        outcome=random.choice(list)
        if outcome== 1 or 2 or 3:
            animate_typing("\nYou dealt hitpoints.")
        else:
            animate_typing("\n\nYou dealt no damage.")

          





    

        
def initiate_combat():
    choices()
