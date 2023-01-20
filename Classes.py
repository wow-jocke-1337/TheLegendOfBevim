from Ascii_Art import*
from Text import*
from items import*

class Player():
    def __init__(self, name, klass, HP, STR, DEX, INT, equipped_weapon):
        self.name = name
        self.lvl = 1
        self.HP = HP
        self.XP = 0
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.inventory = []
        self.klass = klass
        self.equipped_weapon = equipped_weapon
        self.inventory_slots = 4
        
    def attack(self):
        pass
    
    def defend(self):
        pass
    
    def use_item(self):
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
    
    def remove_item(self, item):
        self.inventory.remove(item)

    def print_info(self):
        animate_typing_fast(f"""
            {self.name} the {self.klass}
        HP: {self.HP}
        LVL:{self.lvl}
        XP: {self.XP}
        STR:{self.STR}
        DEX:{self.DEX}
        INT:{self.INT}
        Equipped Weapon:{self.equipped_weapon}
        Inventory:      {self.inventory}
        """)
               

    def print_inventory():
        while True:
            time.sleep(1)
            animate_typing(f"\n\n{Player.inventory}\n")
            animate_typing("\n What do you want to do? ")
            animate_typing(inventory_menu)
            x = int(input(""))

            if x == 1:    #Use
                while True:
                    animate_typing(f"\n{Player.inventory}\n")
                    if len(Player.inventory) > 1:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: 1-{len(Player.inventory)} \n -I dont want to use anything (0) \n \n Your choice --> ")  
                            y = int(input(""))
                            if y == 0:
                                break
                            elif y > len(Player.inventory) or y < 1:
                                animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                                break
                            Player.use_item(y-1)
                            break
                        
                    elif len(Player.inventory) < 2:
                        while True:
                            animate_typing(f"\n Which item do you want to use?  Options: {Player.inventory[0]} (1)  \n -I dont want to use anything (0) \n \n Your choice --> ") 
                            y = int(input(""))
                            if y == 0:
                                break
                            elif y > len(Player.inventory) or y < 1:
                                animate_typing("\nYou only have one item dumbass\n\n")
                                break
                            Player.use_item(y-1)
                            break
                        
            elif x == 2:   #Drop
                if len(Player.inventory) > 1:
                    while True:
                        animate_typing(f"\n\n{Player.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: 1-{len(Player.inventory)} \n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        y = int(input(""))
                        if y == 0:
                            break
                        elif y > len(Player.inventory) or y < 1:
                            animate_typing(f"\n\n You can only choose between item 1-{len(Player.inventory)} Dumbass \n\n")
                        else:
                            animate_typing(f"\n\n are you sure you want to drop the {Player.inventory[y-1]} \n\n yes or no? ")
                            z = (input(""))
                            if z == "yes":
                                animate_typing(f"\n\n ...you dropped the {Player.inventory[y-1]} ...\n\n\n")
                                Player.inventory.pop(y-1)
                            elif z == "no":
                                animate_typing("\n\n\n ok \n\n")
                            break
                elif len(Player.inventory) < 2:
                    while True:
                        animate_typing(f"\n\n{Player.inventory}\n")
                        animate_typing(f"\n Which item do you want to drop?  Options: {Player.inventory[0]} (1)\n -I dont want to drop anything (0) \n\nYour choice --> ") 
                        y = int(input(""))
                        if y == 0:
                            break
                        elif y > len(Player.inventory) or y < 1:
                            animate_typing("\nYou only have one item dumbass\n\n")
                        else:
                            animate_typing(f"\n\n are you sure you want to drop the {Player.inventory[y-1]} \n\n yes or no? ")
                            z = (input(""))
                            if z == "yes":
                                animate_typing(f"\n\n ...you dropped the {Player.inventory[y-1]} ...\n\n\n")
                                Player.inventory.pop(y-1)
                            elif z == "no":
                                animate_typing("\n\n\n ok \n\n")
                            break
                    print("\n")
            elif x == 3:  #go back
                break
            else:
                animate_typing("\n\nyou only have three options dumbass\n\n")
        print("\n")        
        time.sleep(1)
    
    def use_item(x):
        animate_typing(f"\n\n ...you used the {Player.inventory[x]} ...\n\n\n")
        if x == Weapon:
            Player.equipped_weapon = x
            animate_typing(f"\n\n ...the {Player.inventory[x]} is now equiped... \n\n\n")
        
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
        self.STR = 30
        self.DEX = 20
        self.INT = 40
        self.ammo = 15
        self.equipped_weapon = Bow(3+self.DEX*0.5 + self.STR * 0.15)
        self.inventory = [Ammo(10),"Bait"]

class Barbarian(Player):
    def __init__(self, name):
        super().__init__(name, "Barbarian",100,50,25,10)
        self.equipped_weapon = Club(3+self.DEX*0.15 + self.STR * 0.5)
        self.inventory = [Healing_potion(2)]
    pass

class Barbarian():
    def __init__(self) -> None:
        self.klass = "Barbarian"
        self.HP = 100
        self.STR = 50
        self.DEX = 25
        self.INT = 10
        self.equipped_weapon = Club(3+self.DEX*0.15 + self.STR * 0.5)
        self.inventory = [Healing_potion(2),"Rusted Chains"]

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage",60,10,20,50)
        self.equipped_weapon = Magical_Staff(3+self.DEX*0.2 + self.INT * 0.5)
        self.inventory = ["Magic powder(not cocaine) ", "Magic talking Hat"]
    pass

class Mage():
    def __init__(self) -> None:
        self.klass = "Mage"
        self.HP = 60
        self.STR = 10
        self.DEX = 20
        self.INT = 50
        self.equipped_weapon = Magical_Staff(3+self.DEX*0.2 + self.INT * 0.5)
        self.inventory = ["Magic powder(not cocaine) ", "Magic talking Hat"]

class Warrior():
    def __init__(self) -> None:
        self.klass = "Mage"
        self.HP = 60
        self.STR = 10
        self.DEX = 20
        self.INT = 50
        self.equipped_weapon = Magical_Staff(3+self.DEX*0.2 + self.INT * 0.5)
        self.inventory = ["Magic powder(not cocaine) ", "Magic talking Hat"] 

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

class Alfreds_otroligt_Fina_Mamma():
    def __init__(self):
        super().__init__("Alfreds otroligt Fina mamma","The final railing")
        self.lvl = 10
        self.HP = 100000
        self.STR = 10000
        self.inventory = []