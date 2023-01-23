from Ascii_Art import*
from Text import*
from items import*

class Player():
    def __init__(self, name, klass, HP,Defense, STR, DEX, INT, inventory:list):
        self.name = name
        self.lvl = 1
        self.HP = HP
        self.Defense = Defense
        self.XP = 0
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.inventory = inventory
        self.klass = klass
        self.equipped_weapon = None
        self.inventory_slots = 4
        
    def attack(self):
        pass
    
    def defend(self):
        pass
    
    def is_dead(self):
        return self.HP <= 0
    
    def is_level_up(self):
        pass
    
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

    def print_info(self):
        animate_typing(f"""
        {self.name} the {self.klass}
        HP: {self.HP}
        Defense:{self.Defense}
        LVL:{self.lvl}
        XP: {self.XP}
        STR:{self.STR}
        DEX:{self.DEX}
        INT:{self.INT}
        Equipped Weapon:{self.equipped_weapon}
        Inventory:{self.inventory}
        """)            

    def print_inventory(self):
        while True:
            time.sleep(1)
            # animate_typing(f"\n\n{self.inventory}\n")
            for Item in self.inventory:
                animate_typing(f"Item name: {Item.name} ")
            animate_typing("\n What do you want to do? ")
            animate_typing(inventory_menu)
            x = int(input(""))

            if x == 1:    #Use
                    animate_typing(f"\n{self.inventory}\n")
                    if len(self.inventory) > 1:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: 1-{len(self.inventory)} \n -I dont want to use anything (0) \n \n Your choice --> ")  
                            y = int(input(""))
                            if y == 0:
                                break
                            elif y > len(self.inventory) or y < 1:
                                animate_typing(f"\n\n You can only choose between item 1-{len(self.inventory)} Dumbass \n\n")
                                break
                            self.use_item(y-1)
                            break
            
                    elif len(self.inventory) < 2:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: {self.inventory[0]} (1)  \n -I dont want to use anything (0) \n \n Your choice --> ") 
                            y = int(input(""))
                            if y == 0:
                                break
                            elif y > len(self.inventory) or y < 1:
                                animate_typing("\nYou only have one item dumbass\n\n")
                                break                           
                            self.use_item(y-1)
                            break
                        
            elif x == 2:   #Drop
                if len(self.inventory) > 1:
                    while True:
                        animate_typing(f"\n\n{self.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: 1-{len(self.inventory)} \n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        y = int(input(""))
                        if y == 0:
                            break
                        elif y > len(self.inventory) or y < 1:
                            animate_typing(f"\n\n You can only choose between item 1-{len(self.inventory)} Dumbass \n\n")
                        else:
                            animate_typing(f"\n\n WARNING: Are you sure you want to drop the {self.inventory[y-1]} \n\n Yes or No? ")
                            z = (input(""))
                            if z == "yes".lower():
                                animate_typing(f"\n\n ...You dropped the {self.inventory[y-1]} ...\n\n\n")
                                self.inventory.pop(y-1)
                            elif z == "no".lower():
                                animate_typing("\n\n\n Ok \n\n")
                            break
                elif len(self.inventory) < 2:
                    while True:
                        animate_typing(f"\n\n{self.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: {self.inventory[0]} (1)\n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        y = int(input(""))
                        if y == 0:
                            break
                        elif y > len(self.inventory) or y < 1:
                            animate_typing("\nYou only have one item dumbass\n\n")
                        else:
                            animate_typing(f"\n\n Are you sure you want to drop the {self.inventory[y-1]} \n\n Yes or no? ")
                            z = (input(""))
                            if z == "yes".lower():
                                animate_typing(f"\n\n ...you dropped the {self.inventory[y-1]} ...\n\n\n")
                                self.inventory.pop(y-1)
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
        if used_item.klass == "Ranged Weapon" or "Melee Weapon":
            animate_typing(f"\n\nDo you want to equip {used_item} \n\n Yes or No? ")
            equip_choice = int(input(""))
            if equip_choice == "yes".lower():
                animate_typing(f"\n\n ...The {self.inventory[used_item]} is now equipped... \n\n\n")
                self.equip_weapon(used_item)
                self.inventory.pop(used_item)
            elif equip_choice == "no".lower():
                animate_typing("\n\n\n Ok \n\n")          
        else:
            animate_typing(f"\n\n{self.inventory[used_item]} has been used...\n\n\n")
            self.inventory.pop(used_item)
            
    
    
                

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

class Archer():
    def __init__(self) -> None:
        self.klass = "Archer"
        self.HP = 80
        self.Defense = 20
        self.STR = 20
        self.DEX = 40
        self.INT = 10
        self.ammo = 15
        self.inventory = []


class Barbarian():
    def __init__(self) -> None:
        self.klass = "Barbarian"
        self.Defense = 40
        self.HP = 100
        self.STR = 50
        self.DEX = 25
        self.INT = 10
        self.inventory = []

class Mage():
    def __init__(self) -> None:
        self.klass = "Mage"
        self.Defense = 15
        self.HP = 60
        self.STR = 10
        self.DEX = 20
        self.INT = 50
        self.inventory = []

class Warrior():
    def __init__(self) -> None:
        self.klass = "Warrior"
        self.Defense = 35
        self.HP = 120
        self.STR = 35
        self.DEX = 35
        self.INT = 20
        self.inventory = []

class Monster():
    def __init__(self, name, klass):
        self.name = name
        self.lvl = 1
        self.HP = 100
        self.XP = 0 
        self.STR = 10
        self.INT = 10
        self.DEX = 10
        self.inventory = []
        self.klass = klass
        self.equipped_weapon = None
        self.inventory_slots = 4

class Wolf():
    def __init__(self):
        super().__init__("Wolf","Animal")
        self.lvl = 1
        self.HP = 24
        self.STR = 3
        self.inventory = []

class Golem(Monster):
    def __init__(self):
        super().__init__("Golem", "Strong boi")
        self.lvl = 4
        self.HP = 6000
        self.STR = 150
        self.inventory = []

class slime(Monster):
    def __init__(self):
        super().__init__("Slime", "Mob")
        self.lvl = 1
        self.HP = 7
        self.STR = 8
        self.inventory = []

class mountain_Lion(Monster):
    def __init__(self):
        super().__init__("Mountain Lion", "Animal")
        self.lvl = 3
        self.HP = 45
        self.STR = 5
        self.inventory = []

class Bats(Monster):
    def __init__(self):
        super().__init__("Bats", "Mob")
        self.lvl = 2
        self.HP = 2
        self.STR = 1
        self.inventory = []

class archdemon(Monster):
    def __init__(self):
        super().__init__("Archdemon", "Boss")
        self.lvl = 7
        self.HP = 50000
        self.STR = 400
        self.inventory = []

class Bevins_bror(Monster):
    def __init__(self):
        super().__init__("Bevins Bror","Boss")
        self.lvl = 9
        self.HP = 85000
        self.STR = 1400
        self.inventory = []

class Bevins_otroligt_Fina_Mamma():
    def __init__(self):
        super().__init__("Alfreds otroligt Fina mamma","The final railing")
        self.lvl = 10
        self.HP = 100000
        self.STR = 10000
        self.inventory = []