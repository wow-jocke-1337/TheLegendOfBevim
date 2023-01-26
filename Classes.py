from Ascii_Art import*
from Text import*
from items import*

class Player():
    def __init__(self, name, klass, HP, lvl, Def, spd, STR, DEX, INT, inventory:list):
        self.name = name
        self.lvl = lvl
        self.klass = klass
        self.HP = HP
        self.Def = Def
        self.spd = spd
        self.XP = 0
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.inventory = inventory
        self.equipped_weapon = None
        self.inventory_slots = 4
        
    def attack(self):
        pass
    
    def defend(self):
        pass
    
    def is_dead(self):
        return self.HP <= 0
    
    def can_use_item(self, item): 
        pass
    
    def add_item(self, item):
        if len(self.inventory) < self.inventory_slots:
            self.inventory.append(item)
        else:
            print("Inventory full!")
        pass

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        
    def calculate_damage(self):
        if self.equipped_weapon is None:
            return 0
        else:
            return self.STR * self.equipped_weapon.str_mod + self.DEX * self.equipped_weapon.dex_mod + self.INT * self.equipped_weapon.int_mod
    
    def remove_item(self, item):
        self.inventory.remove(item)

    def print_items(self):
        for Item in self.inventory:
            animate_typing(f"Item name: {Item.name}")

    def print_info(self):
        animate_typing(f"""
        -----------------------------------------
        {self.name} the {self.klass}
        Def: {self.Def}
        HP:  {self.HP}
        LVL: {self.lvl}
        XP:  {self.XP}
        Speed:{self.spd}
        STR: {self.STR}
        DEX: {self.DEX}
        INT: {self.INT}
        Equipped Weapon: {self.equipped_weapon}
        Inventory: {self.inventory}
        ------------------------------------------""")            

    def print_inventory(self):
        while True:
            time.sleep(1)
            animate_typing(f"\n\n{self.inventory}\n")
            animate_typing("\n\n What do you want to do? ")
            animate_typing(inventory_menu)
            x = int(input(""))

            if x == 1:    #Use
                    animate_typing(f"\n{self.inventory}\n")
                    if len(self.inventory) > 1:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: 1-{len(self.inventory)} \n -I dont want to use anything (0) \n \n Your choice --> ")  
                            item_choice = int(input(""))
                            if item_choice == 0:
                                break
                            elif item_choice > len(self.inventory) or item_choice < 1:
                                animate_typing(f"\n\n You can only choose between item 1-{len(self.inventory)} Dumbass \n\n")
                                break
                            self.use_item(self.inventory[item_choice-1])
                            break            
                    elif len(self.inventory) < 2:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: {self.inventory[0]} (1)  \n -I dont want to use anything (0) \n \n Your choice --> ") 
                            item_choice = int(input(""))
                            if item_choice == 0:
                                break
                            elif item_choice > len(self.inventory) or item_choice < 1:
                                animate_typing("\nYou only have one item dumbass\n\n")
                                break                           
                            self.use_item(self.inventory[item_choice-1])
                            break                        
            elif x == 2:   #Drop
                if len(self.inventory) > 1:
                    while True:
                        animate_typing(f"\n\n{self.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: 1-{len(self.inventory)} \n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        item_choice = int(input(""))
                        if item_choice == 0:
                            break
                        elif item_choice > len(self.inventory) or item_choice < 1:
                            animate_typing(f"\n\n You can only choose between item 1-{len(self.inventory)} Dumbass \n\n")
                        else:
                            animate_typing(f"\n\n Are you sure you want to drop the {self.inventory[item_choice-1]} \n\n Yes or No? ")
                            z = (input(""))
                            if z == "yes".lower():
                                animate_typing(f"\n\n ...You dropped the {self.inventory[item_choice-1]} ...\n\n\n")
                                self.inventory.pop(item_choice-1)
                            elif z == "no".lower():
                                animate_typing("\n\n\n Ok \n\n")
                            break
                elif len(self.inventory) < 2:
                    while True:
                        animate_typing(f"\n\n{self.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: {self.inventory[0]} (1)\n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        item_choice = int(input(""))
                        if item_choice == 0:
                            break
                        elif item_choice > len(self.inventory) or item_choice < 1:
                            animate_typing("\nYou only have one item dumbass\n\n")
                        else:
                            animate_typing(f"\n\n Are you sure you want to drop the {self.inventory[item_choice-1]} \n\n Yes or no? ")
                            z = (input(""))
                            if z == "yes".lower():
                                animate_typing(f"\n\n ...you dropped the {self.inventory[item_choice-1]} ...\n\n\n")
                                self.inventory.pop(item_choice-1)
                            elif z == "no".lower:
                                animate_typing("\n\n\n Ok \n\n")
                            break
                    print("\n")
            elif x == 3:  #go back
                break
            else:
                animate_typing("\n\nYou only have three options dumbass\n\n")
        print("\n")
        time.sleep(1)
    
    def use_item(self, used_item):
        if isinstance(used_item,Weapon):
            animate_typing(f"\n\nDo you want to equip {used_item} \n\n Yes or No? ")
            equip_choice = input("")
            if equip_choice == "yes".lower():
                animate_typing(f"\n\n ...The {used_item} is now equipped... \n\n")
                self.equip_weapon(used_item)
                self.inventory.remove(used_item)
            elif equip_choice == "no".lower():
                animate_typing("\n\n Ok")
        elif isinstance(used_item,Healing_Item):
            self.use_healing_item(used_item)
            animate_typing(f"\n\nDo you want to drink {used_item} \n\n Yes or No? ")
            drink_choice = input("")
            if drink_choice =="yes".lower():
                animate_typing(f"\n\n....You drank the {used_item} ....\n\n")
                self.inventory.remove(used_item)
            elif drink_choice =="no".lower():
                animate_typing(f"\n\n Ok")
        else:
            animate_typing(f"\n\nYou cannot use this \n\n")

    def attack():
        pass
       # Här sker "eldväxlingen"

    def Block():
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def add_xp(self,enemy):
        self.XP += enemy

    def add_item(self,enemy_item):
        self.inventory.append(enemy_item)
        pass
        # här läggs nånting in i spelarens inventory

    def lvl_up(self):
        if self.lvl >= 100:
            self.lvl += 1
       # Här ska lvl öka

    def take_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:
            return exit()
        # Här ska antalet liv minska

    def use_healing_item(self,Item):
        if isinstance (Item, Healing_Item):
            health_increase = (float(self.HP) * Item.effect)
            self.HP += health_increase
            animate_typing(f"\nYour health has increased by {health_increase} points.")
        elif isinstance (Item, Resource_Item):
            animate_typing(f"\nYou drank {self.name}")

class Archer():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Archer"
        self.HP = 80
        self.Def = 20
        self.STR = 20
        self.DEX = 40
        self.INT = 10
        self.spd = 17
        self.inventory = []

class Gunslinger():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Gunslinger"
        self.HP = 90        
        self.Def = 20
        self.STR = 15
        self.DEX = 45
        self.INT = 10
        self.spd = 20
        self.inventory = []

class Barbarian():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Barbarian"
        self.Def = 40       
        self.HP = 100
        self.STR = 50
        self.DEX = 25
        self.INT = 10
        self.spd = 15
        self.inventory = []

class Mage():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Mage"
        self.Def = 15
        self.HP = 60
        self.STR = 10
        self.DEX = 20
        self.INT = 50
        self.spd = 12
        self.inventory = []

class Warrior():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Warrior"
        self.Def = 35
        self.HP = 120
        self.STR = 35
        self.DEX = 35
        self.INT = 20
        self.spd = 12
        self.inventory = ["Bing chiulling"]

class Monster():
    def __init__(self, name,lvl, xp,klass,HP,STR,spd,equipped_weapon):
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.HP = HP
        self.STR = STR
        self.spd = spd
        self.inventory = []
        self.klass = klass
        self.equipped_weapon = equipped_weapon
        self.inventory_slots = 1
    
    def __repr__(self) -> None:
        animate_typing (f"""
        {self.name}
        Health:{self.HP}
        Level: {self.lvl}
        Strength: {self.STR}
        Speed: {self.spd}
        """)
    
    def take_damage(self, damage):
        self.HP -= damage

    def is_dead(self):
        if self.HP < 0:
            return self.HP <= 0
    
    def attack(self):
        pass


class wolf(Monster):
    def __init__(self):
        super().__init__("Wolf",2,25,"low_Mob",90,30,15,None)

class golem(Monster):
    def __init__(self):
        super().__init__("Golem",2,33,"low_Mob",140,20,5,"Boulder")

class slime(Monster):
    def __init__(self):
        super().__init__("Slime",1,20,"low_Mob",75,20,10,None)

class goblin(Monster):
    def __init__(self):
        super().__init__("Goblin",1,20,"low_Mob",75,20,10,"Crooked Knife")

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 3, 35,"low_mob", 100, 35, 13,"Two-Handed Axe")

class mountain_Lion(Monster):
    def __init__(self):
        super().__init__("Mountain Lion",2,30,"low_Mob",95,30,15,None)

class bats(Monster):
    def __init__(self):
        super().__init__("Bats",1,20,"low_Mob",60,20,10,None)

class dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 5, 37,"Mid tier mob", 140, 55, 10, None)

class lower_class_demon(Monster):
    def __init__(self) -> None:
        super().__init__("Lower Class Demon",5,37,"Mid tier mob",130,47,13,"Longsword of Night and Flame")

class kikimora(Monster):
    def __init__(self):
        super().__init__("Kikimora",5,35,"Mid tier mob",140,50,10,None)

class bruxa(Monster):
    def __init__(self):
        super().__init__("Bruxa",6,40,"Mid tier mob",145,50,13,None)

class upper_class_demon(Monster):
    def __init__(self) -> None:
        super().__init__("Upper Class Demon",6,42,"Mid tier mob",140,55,15,"Moonsword")

class archdemon(Monster):
    def __init__(self):
        super().__init__("Archdemon",8,47,"Boss",170,70,15,"Taeshalach the Souleater")

class bevins_bror(Monster):
    def __init__(self):
        super().__init__("Bevins bror",69,666,"Boss",200,65,20,"Gaming chair")

class bevins_mamma(Monster):
    def __init__(self):
        super().__init__("Bevins Mamma",666,69420,"The End",420,33,6.9,"Child Beater 9000")