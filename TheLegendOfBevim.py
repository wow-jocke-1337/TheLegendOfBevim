import random as rand
from Classes import*
from Ascii_Art import*
from Text import*



while True:
    x = int(input("""
Välkommen till THE LEGEND OF BEVIM
    """))
    if x == 1:
        pass
    elif x == 2:
        pass

    namn = input("Vad är ditt namn? ")
    
    player = Player(namn)       # Initiera en spelare med namnet namn



    player.get_attacked()
    if player.HP < 0:
         break
        
