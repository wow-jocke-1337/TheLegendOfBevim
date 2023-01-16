from Ascii_Art import*
from Text import*

class Player():
    name = ""
    lvl = 1
    HP = 0
    XP = 0 
    STR = 0
    INT = 0
    DEX = 0
    inventory = []
    inventory_slots = 4
    klass = ""

    def print_info():
        animate_typing_fast(f""" 
        {Player.name} the {Player.klass}
        LVL:  {Player.lvl}
        XP:   {Player.XP}
        HP:   {Player.HP}
        Strength: {Player.STR}
        Intelligence: {Player.INT}
        Dexterity: {Player.DEX}
        Inventory slots: {Player.inventory_slots}

        """)

    

    def print_inventory():
        time.sleep(1)
        animate_typing(f"\n\n{Player.inventory}\n")
        while True:
            animate_typing("\n What do you want to do? ")
            animate_typing(inventory_menu)
            x = int(input(""))
            if x == 1:    #Use
                while True:
                    animate_typing(f"\n{Player.inventory}\n")
                    if len(Player.inventory) > 1:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: 1-{len(Player.inventory)} \n \n Your choice --> ")  
                            y = int(input(""))
                            if y > len(Player.inventory) or y < 0:
                                animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                                break
                            elif y > len(Player.inventory) or y < 0 and len(Player.inventory) < 2:
                                animate_typing("\nYou only have one item dumbass\n\n")
                                break  
                            Player.use_item(y)
                            break
                    elif len(Player.inventory) < 2:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: {Player.inventory[0]} (1) \n \n Your choice --> ") 
                            y = int(input(""))
                            if y > len(Player.inventory) or y < 0:
                                animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                                break
                            elif y > len(Player.inventory) or y < 0 and len(Player.inventory) < 2:
                                animate_typing("\nYou only have one item dumbass\n\n")
                                break
                            Player.use_item(y)
                            break
                    break
            elif x == 2:   #Drop
                if len(Player.inventory) > 1:
                    while True:
                        animate_typing(f"\n\n{Player.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: 1-{len(Player.inventory)} \n \n Your choice --> ") 
                        y = int(input(""))
                        if y > len(Player.inventory) or y < 1:
                            animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                        elif y > len(Player.inventory) or y < 1 and len(Player.inventory) < 2:
                            animate_typing("\nYou only have one item dumbass\n\n")
                        animate_typing(f"\n\n are you sure you want to drop the {Player.inventory[y]} \n\n yes or no? ")
                        z = (input(""))
                        if z == "yes":
                            animate_typing(f"\n\n ...you dropped the {Player.inventory[y]} ...\n\n\n")
                            Player.inventory.pop(y-1)
                        elif z == "no":
                            animate_typing("\n\n\n ok \n\n")
                        break
                elif len(Player.inventory) < 2:
                    while True:
                        animate_typing(f"\n\n{Player.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: {Player.inventory[0]} (1)\n \n Your choice --> ") 
                        y = int(input(""))
                        if y > len(Player.inventory) or y < 1:
                            animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                            break
                        elif y > len(Player.inventory) or y < 1 and len(Player.inventory) < 2:
                            animate_typing("\nYou only have one item dumbass\n\n")
                            break
                        animate_typing(f"\n\n are you sure you want to drop the {Player.inventory[y]} \n\n yes or no? ")
                        z = (input(""))
                        if z == "yes":
                            animate_typing(f"\n\n ...you dropped the {Player.inventory[y]} ...\n\n\n")
                            Player.inventory.pop(y-1)
                        elif z == "no":
                            animate_typing("\n\n\n ok \n\n")
                        break
                        

            elif x == 3:  #go back
                break
            else:
                animate_typing("\n\nyou only have three options dumbass\n\n")
    
    def use_item(y):
        animate_typing(f"\n\n ...you used the {Player.inventory[y-1]} ...\n\n\n")


    def attack():
        pass
       # Här sker "eldväxlingen"

    def Block():
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def add_item():
        pass
        # här läggs nånting in i spelarens inventory
    def lvl_up(): 
        pass
       # Här ska lvl öka

    def gets_attacked():
        pass
        # Här ska antalet liv minska

    def Drink_potion():
        pass

    def Eat_food():
        pass

    def die():
        pass

class Monster():
    lvl = 0
    HP = 0
    STR = 0


class Wolf():
    lvl = 0
    HP = 10
    STR = 2

class Golem():
    lvl = 0
    HP = 30
    STR = 0.5

class slime():
    lvl = 0
    HP = 7
    STR = 3

class mountain_Lion():
    lvl=0
    HP=45
    STR=5

class Bats():
    lvl=0
    HP=2
    STR=1

class archdemon():
    lvl=0
    HP=70
    STR=10.5

class Bevins_bror():
    lvl=0
    HP=100
    STR=8