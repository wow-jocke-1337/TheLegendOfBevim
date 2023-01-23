from Classes import*
from Text import*
from Funktioner import*
from exploring import*

list = [1,2,3,4,5,6]

def attack():
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3 or 4:
            animate_typing("\nYou hit the target!")
        else:
            animate_typing("\nYou missed.")

def block():
        outcome=random.choice(list)
        if outcome==1 or 2 or 3:
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
        elif x==2:
            block()
        elif x==3:
            Player.print_inventory()
            time.sleep(2)
        elif x==4:





def damage():
    while True:
        outcome=random.choice(list)
        if outcome== 1 or 2 or 3:
            animate_typing("\nYou dealt "+ {Player.STR} * 0.25)
            

          





    

        
def initiate_combat():
    choices()

initiate_combat()