import random as rand
from Classes import*
from Ascii_Art import*
from Text import*
from Funktioner import*

animate_typing_fast(startText)
time.sleep(2)
print(gameTitle)

Player()

time.sleep(2)
Player.name = input(animate_typing("Vad är ditt namn? "))    # Initiera en spelare med namnet namn  

x = int(input(Menu))
if x == 1:
    Player.print_info()
elif x == 2:
    pass


Player.gets_attacked()
if Player.HP < 0:
    Player.die
    
exit()