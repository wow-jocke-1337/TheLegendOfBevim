import random as rand
from Ascii_Art import*
from Text import *
from Classes import *
from exploring import *
from Rum import *

archer = Archer()
barbarian = Barbarian()
mage = Mage()
warrior = Warrior()
gunslinger = Gunslinger()



animate_typing_asciispeed(startText)
time.sleep(1)
print(gameTitle)

time.sleep(2)
animate_typing("What is your to be chosen name")
user_name = input("? ")    

time.sleep(1)

while True:
    animate_typing("""

    Kindly choose one of the presented classes. 
        
        1. Barbarian
        2. Archer
        3. Mage
        4. Warrior
        5. Gunslinger

    Your choice --> """)

    klass_choice = input("")
    BARBARIAN = "1"
    ARCHER = "2"
    MAGE = "3"
    WARRIOR = "4"
    GUNSLINGER = "5"
    
    if klass_choice == BARBARIAN:
        player = Player(user_name, "Barbarian", barbarian.HP,barbarian.Def, barbarian.STR, barbarian.DEX, barbarian.INT, barbarian.inventory)
        player.inventory.append(Axe())
        break
    elif klass_choice == ARCHER:
        player = Player(user_name, "Archer", archer.HP,archer.Def, archer.STR, archer.DEX, archer.INT, archer.inventory)
        player.inventory.append(Bow())
        break
    elif klass_choice == MAGE:
        player = Player(user_name, "Mage", mage.HP,mage.Def, mage.STR, mage.DEX, mage.INT, mage.inventory)
        player.inventory.append(Mana_potion())
        player.inventory.append(Magical_staff())
        break
    elif klass_choice == WARRIOR:
        player = Player(user_name, "Warrior", warrior.HP,warrior.Def, warrior.STR, warrior.DEX, warrior.INT, warrior.inventory)
        player.inventory.append(Greatsword())
        break
    elif klass_choice == GUNSLINGER:
        player = Player(user_name, "Gunslinger",gunslinger.HP,gunslinger.Def,gunslinger.DEX,gunslinger.INT,gunslinger.STR,gunslinger.inventory)
    else:
        animate_typing("\n You can only choose between 1-4\n")
        break

player.inventory.append(Healing_potion())


time.sleep(1)
animate_typing_slow(f"""

Welcome {player.name} the {player.klass}

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
        player.print_info()
        time.sleep(2)
    elif x == 2:
        intiate_explore()  
    elif x == 3:
        player.print_inventory()
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