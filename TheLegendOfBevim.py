import random as rand
from Classes import*
from Ascii_Art import*
from Text import*

a_player = Player(3)       # Initiera en spelare med tre liv

while True:
    x = int(input("""
Välkommen till THE LEGEND OF BEVIM
    """))
    if x == 1:
        pass
    elif x == 2:
        pass

    a_player.get_shot()
    if a_player.lifes < 0:
        break

print("Haha du dog :)")

if Player == 1:
    print(f"Haha sämst bitch")