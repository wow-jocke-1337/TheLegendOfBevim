import random as rand
from Classes import*
from Ascii_Art import*
from Text import*
from Funktioner import*
from combat import*
from exploring import*

animate_typing_fast(startText)
time.sleep(2)
animate_typing_asciispeed(gameTitle)

Player()

time.sleep(2)
animate_typing("Vad är ditt namn")
Player.name = input("? ")   # Initiera en spelare med namnet namn  

time.sleep(1.5)
print(f"""

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
        intiate_exploring()
    elif x == 3:
        pass
    elif x == 4:
        animate_typing(credits)
        time.sleep(2)
    elif x == 5:
        animate_typing("""
    Thank you for playing :) 
    
    """)
        exit()


Player.gets_attacked()
if Player.HP < 0:
    Player.die
    
