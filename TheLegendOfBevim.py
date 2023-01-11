import random as rand
from Classes import*
from Ascii_Art import*
from Text import*
from Funktioner import*
from combat import*
from exploring import*

animate_typing_asciispeed(startText)
time.sleep(1)
animate_typing_asciispeed(gameTitle)

Player()

time.sleep(2)
animate_typing("Vad är ditt namn")
Player.name = input("? ")   # Initiera en spelare med namnet namn  



time.sleep(1.5)
animate_typing("""

Vad är du för class? 
    
    Barbarian(1) prostituerad(2) mage(3) 

your choice --> """)

x = int(input(""))
if Player.name == "krille" or "algot" or "agge" or "gabriel" or "gabbe":
    Player.klass = "bög terrorist"
elif x == 1:
    Player.klass = "barbarian"
elif x == 2:
    Player.klass = "prostituerad"
elif x == 3:
    Player.klass = "mage"

time.sleep(1.5)
animate_typing(f"""

Weclome {Player.name} the {Player.klass}

""")

time.sleep(2)

while True:
    animate_typing(Menu)
    x = int(input(""))
    if x == 1:
        Player.print_info()
        time.sleep(2)
    elif x == 2:
        intiate_explore()  
    elif x == 3:
        Player.print_inventory()
        time.sleep(2)
    elif x == 4:
        animate_typing(credits)
        time.sleep(2)
    elif x == 5:
        animate_typing("""
    Thank you for playing :) 

    """)
        exit()
    else:
        animate_typing("""
    You faking stopid choose an actual alternative, not dreaming.
    You should get a mirror, so you can see how dumb you are.
    
    """)