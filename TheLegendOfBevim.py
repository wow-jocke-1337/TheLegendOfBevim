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
animate_typing(f"""

Weclome {Player.name}

""")
time.sleep(1.5)

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