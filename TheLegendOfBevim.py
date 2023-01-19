import random as rand
from Classes import*
from Ascii_Art import*
from Text import*
from Funktioner import*
from combat import*
from exploring import*
from Rum import*

animate_typing_asciispeed(startText)
time.sleep(1)
print(gameTitle)

Player()

time.sleep(2)
animate_typing("Vad är ditt namn")
Player.name = input("? ")    



time.sleep(1)

while True:
    animate_typing("""

    Vad är du för class? 
        
        Barbarian(1) Archer(2) mage(3) 

    your choice --> """)

    klass_choice = int(input(""))
    #if Player.name == "krille" or "krille cum" or "algot" or "agge" or "gabriel" or "gabbe":
    # Player.klass = "Prostituerad"

    if klass_choice == 1:
        Player.klass = "Barbarian"
        Player.HP = 11
        Player.STR = 50
        Player.DEX = 20
        Player.INT = 5
        healing_potions = "Healing potions", 2
        Player.inventory = ["Club ", healing_potions,]
        break
    elif klass_choice == 2:
        Player.klass = "Archer"
        Player.HP = 8
        Player.STR = 20
        Player.DEX = 40
        Player.INT = 35
        arrows = "arrows", 10
        Player.inventory = ["Bow ", arrows, "Bait"]
        break
    elif klass_choice == 3:
        Player.klass = "Mage"
        Player.HP = 6
        Player.STR = 5
        Player.DEX = 30
        Player.INT = 60
        Player.inventory = ["Magical staff ", "magic powder(not cocaine) ", "magic talking Hat"]
        break
    else:
        animate_typing("\n du kan bara välja 1-3\n")

time.sleep(1)
animate_typing_slow(f"""

Welcome {Player.name} the {Player.klass}

""")


time.sleep(1)
Menu = """ 

    MENU
1 - See stats
2 - Explore
3 - Inventory
4 - See credits
5 - Exit game


Your choice --> """

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