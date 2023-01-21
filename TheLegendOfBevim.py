import random as rand
from Ascii_Art import*
from Text import*
from Classes import*
from exploring import*
from Rum import*

archer = Archer()
barbarian = Barbarian()
mage = Mage()
warrior = Warrior()

animate_typing_asciispeed(startText)
time.sleep(1)
print(gameTitle)

time.sleep(2)
animate_typing("Vad är ditt namn")
user_name = input("? ")    

time.sleep(1)

#class_dict = {1: Barbarian, 2: Archer, 3: Mage}

while True:
    animate_typing("""

    Vad är du för class? 
        
        1. Barbarian
        2. Archer
        3. Mage
        4. Warrior

    your choice --> """)

    klass_choice = input("")
    BARBARIAN = "1"
    ARCHER = "2"
    MAGE = "3"
    WARRIOR = "4"
    # if klass_choice.isdigit() and 1 <= int(klass_choice) <= 3:
    #    Player.klass = class_dict[int(klass_choice)](Player.name)
    if klass_choice == BARBARIAN:
        player = Player(user_name, "Barbarian", barbarian.HP, barbarian.STR, barbarian.DEX, barbarian.INT, barbarian.inventory)
        break
    elif klass_choice == ARCHER:
        player = Player(user_name, "Archer", archer.HP, archer.STR, archer.DEX, archer.INT, archer.inventory)
        break
    elif klass_choice == MAGE:
        player = Player(user_name, "Mage", mage.HP, mage.STR, mage.DEX, mage.INT, mage.inventory)
        break
    elif klass_choice == WARRIOR:
        player = Player(user_name, "Warrior", warrior.HP, warrior.STR, warrior.DEX, warrior.INT, warrior.inventory)
        break
    else:
        animate_typing("\n du kan bara välja 1-3\n")
        break


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