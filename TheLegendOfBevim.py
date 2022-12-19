import random as rand
from Classes import*
from Ascii_Art import*
from Text import*
from Funktioner import*

animate_typing_fast(startText)
time.sleep(2)
animate_typing_asciispeed(gameTitle)

Player()

time.sleep(2)
animate_typing("Vad är ditt namn")
Player.name = input("? ")   # Initiera en spelare med namnet namn  

while True:
    animate_typing(Menu)
    x = int(input(""))
    if x == 1:
        Player.print_info()
        time.sleep(2)
    elif x == 2:
        break
    elif x == 3:
        animate_typing("""
    Thank you for playing :) 
    
    """)
        exit()


Player.gets_attacked()
if Player.HP < 0:
    Player.die
    
