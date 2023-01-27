from Ascii_Art import*
from Text import*
from items import*

class Player():
    def __init__(self, name, klass, current_HP, max_HP, lvl, Def, agility, STR, DEX, equipped_weapon,INT, inventory:list):
        self.name = name
        self.lvl = lvl
        self.klass = klass
        self.current_HP = current_HP
        self.max_HP = max_HP
        self.Def = Def
        self.agility = agility
        self.XP = 0
        self.XP_to_level_up = 100
        self.money_at_hand = 20
        self.STR = STR
        self.INT = INT
        self.DEX = DEX
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon
        self.inventory_slots = 420

    
    def is_dead(self):
        if self.current_HP < 0:
            return True
        else:
            return False
    
    def can_buy_item(self, item):
        pass
    
    def add_item(self, item):
        if len(self.inventory) < self.inventory_slots:
            self.inventory.append(item)
        else:
            animate_typing("Inventory full!")

    def equip_weapon(self, weapon):
        if self.equipped_weapon == None:
            self.equipped_weapon = weapon
        else:
            self.inventory.append(self.equipped_weapon)
            self.equipped_weapon = weapon
        
    def calculate_damage(self):
        if self.equipped_weapon is None:
            return 0
        else:
            return int(self.STR * self.equipped_weapon.str_mod + self.DEX * self.equipped_weapon.dex_mod + self.INT * self.equipped_weapon.int_mod)
    
    def remove_item(self, item):
        self.inventory.remove(item)

    def print_info(self):
        animate_typing(f"""
-----------------------------------------
{self.name} the {self.klass} 
LVL: {self.lvl}  XP: {self.XP}
HP: Current: {self.current_HP}  
    Maximum: {self.max_HP}

Def    {self.Def}
STR    {self.STR}
DEX    {self.DEX}
INT    {self.INT}
Agil   {self.agility}

Equipped Weapon: {self.equipped_weapon}
INVENTORY {self.inventory}
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
                            animate_typing(f"\n\n Are you sure you want to drop the {self.inventory[item_choice-1]} \n\n Yes or no? \n Your choice--> ")
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
            if self.equipped_weapon == None:
                animate_typing(f"\n\nDo you want to equip {used_item}? \n\n Yes or no? \n Your choice--> ")
                equip_choice = input("")
                if equip_choice == "yes".lower():
                    animate_typing(f"\n\n ...The {used_item} is now equipped... \n\n")
                    self.equip_weapon(used_item)
                    self.inventory.remove(used_item)
                elif equip_choice == "no".lower():
                    animate_typing("\n\n Ok")
            else:
                animate_typing(f"\n\nDo you want to equip {used_item} and replace {self.equipped_weapon}? \n\n Yes or no? \n Your choice--> ")
                equip_choice = input("")
                if equip_choice == "yes".lower():
                    animate_typing(f"\n\n ...The {used_item} is now equipped... \n\n")
                    self.inventory.append(self.equipped_weapon)
                    self.equip_weapon(used_item)
                    self.inventory.remove(used_item)
                elif equip_choice == "no".lower():
                    animate_typing("\n\n Ok")
        elif isinstance(used_item,Healing_Item):
            if self.current_HP == self.max_HP:
                animate_typing("\n\n...you already have max HP...\n\n")
            else:
                animate_typing(f"\n\n\n Current HP {self.current_HP} Max HP {self.max_HP} \n\n Do you want to drink {used_item} \n\n Yes or No? ")
                drink_choice = input("")
                if drink_choice =="yes".lower():
                    animate_typing(f"\n\n....You drank the {used_item} ....\n\n")
                    self.use_healing_item(used_item)
                    self.inventory.remove(used_item)
                elif drink_choice =="no".lower():
                    animate_typing(f"\n\n Ok")
        else:
            animate_typing(f"\n\nYou cannot use this \n\n")

    def player_Attack(self,enemy):
        #calculate damage dealt to the enemy and check if you missed or landed a hit.
        hit_chance = random.randint(1,100)
        if self.agility > enemy.agility:
            if hit_chance > 30:
                player_damage = self.calculate_damage()
                enemy.take_damage(player_damage)
                if self.klass == "Gunslinger":
                    ability = random.choice(self.equipped_weapon.abilities)
                    animate_typing(f"\n{ability}!")
                    animate_typing(f"\n{self.name} swiftly drew, and damaged the {enemy.name} for {player_damage} damage.\n")
                    animate_typing("\nSSS rank. Smoking, Sexy, Style!!!\n")
                elif self.klass == "Mage":
                    ability = random.choice(self.equipped_weapon.abilities)
                    animate_typing(f"\n{ability}!")
                    animate_typing(f"\n{self.name} cast a spell, damaging the {enemy.name} for {player_damage} damage.\n")
                    animate_typing("\nStylish!\n")
                elif self.klass == "Warrior":
                    ability = random.choice(self.equipped_weapon.abilities)
                    animate_typing(f"\n{ability}!")
                    animate_typing(f"\n{self.name} landed a heavy blow on the {enemy.name} for {player_damage} damage.\n")
                    animate_typing("\nSSS rank. Smoking, Sexy, Style!!!\n")
                elif self.klass == "Barbarian":
                    ability = random.choice(self.equipped_weapon.abilities)
                    animate_typing(f"\n{ability}!")
                    animate_typing(f"\n{self.name} landed a hit the on the {enemy.name} for {player_damage} damage.\n")
                    animate_typing("\nSSS rank. Smoking, Sexy, Style!!!\n")
                elif self.klass == "Archer":
                    ability = random.choice(self.equipped_weapon.abilities)
                    animate_typing(f"\n{ability}!")
                    animate_typing(f"\n{self.name} landed a hit the on the {enemy.name} for {player_damage} damage.\n")
                    animate_typing("\nSSS rank. Smoking, Sexy, Style!!!\n")
            else:
                animate_typing("\nYou missed!")
        else:
            if hit_chance < 80:
                player_damage = self.calculate_damage()
                enemy.take_damage(player_damage)
                animate_typing(f"\nYou hit the {enemy.name} for {player_damage} damage.\n")
            else:
                animate_typing(f"\nYou missed!\n")
    
    def dodge(self,enemy):
        dodge_chance = random.randint(1,100)
        if self.agility > enemy.agility:
            if dodge_chance > 30:
                return True
            else:
                return False
        else:
            if dodge_chance < 30:
                return True
            else:
                return False

    def player_run(self):
        #calculate chance to run away from combat
        run_chance = random.randint(1,100)
        if run_chance > 50: #50% chance to run
            animate_typing("\nYou successfully ran away!")
            return True
        else:
            animate_typing("\nYou failed to run away.")
            return False

    def add_xp(self, enemy_xp):
        self.XP += enemy_xp
        if self.XP >= self.XP_to_level_up:
            self.lvl_up()

    def add_item(self,enemy_item):
        self.inventory.append(enemy_item)
        pass
        # här läggs nånting in i spelarens inventory

    def lvl_up(self):
        self.lvl += 1
        self.XP_to_level_up = self.lvl * 50
        if self.klass == "Archer":
            self.DEX += 3
            self.STR += 1
            self.INT += 1
            self.max_HP += 12
            self.current_HP = self.max_HP
        elif self.klass == "Warrior":
            self.DEX += 2
            self.STR += 3
            self.INT += 1
            self.max_HP += 12
            self.current_HP = self.max_HP
            self.DEX = int
            self.STR = int
        elif self.klass == "Mage":
            self.DEX += 1
            self.STR += 1
            self.INT += 3
            self.max_HP += 12
            self.current_HP = self.max_HP
        elif self.klass == "Barbarian":
            self.DEX += 1
            self.STR += 3
            self.INT += 1
            self.max_HP += 12
            self.current_HP = self.max_HP
        elif self.klass == "Gunslinger":
            self.DEX += 3
            self.STR += 1
            self.INT += 2
            self.max_HP += 12
            self.current_HP = self.max_HP
       # Här ska lvl öka

    def take_damage(self, damage):
        self.current_HP = int(self.current_HP - damage)
        if self.current_HP < 0:
            animate_typing("\nYou died....... Git Gud.\n")
            exit()
        else:
            return self.current_HP
        # Här ska antalet liv minska
    

    def block(self,enemy_damage):
        block_damage_multiplier = random.randint(1,3)
        block_damage = (block_damage_multiplier/10) * self.STR
        damage_blocked = int(block_damage - enemy_damage)
        if damage_blocked > 0:
            animate_typing(f"\n{self.name} successfully blocked.\n")
            return True
        else:
            animate_typing(f"\nYour block did not go through\n")
            animate_typing(f"\n{self.name} lost {enemy_damage} hp.\n")
            self.current_HP = self.current_HP - enemy_damage
            return False
        #Här ska chansen att blockera beräknas och returnera som Falsk eller Sant samt HP.


    def use_healing_item(self,Item):
        if isinstance (Item, Healing_Item):
            health_increase = int(self.current_HP * Item.healing_effect)
            self.current_HP += health_increase
            if self.current_HP > self.max_HP:
                self.current_HP = self.max_HP
                animate_typing(f"\n{Item.name} used.")
                animate_typing(f"...Your health has increased by {health_increase} points...\n{self.name}s HP: {self.current_HP}/{self.max_HP}")
        elif isinstance (Item, Resource_Item):
            animate_typing(f"\n{Item.name} used.\n")

class Barbarian():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Barbarian"
        self.Def = 40       
        self.current_HP = 100
        self.max_HP = 100
        self.STR = 50
        self.DEX = 25
        self.INT = 10
        self.agility = 15
        self.inventory = []
        self.equipped_weapon = Axe()
class Archer():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Archer"
        self.Def = 20
        self.current_HP = 80
        self.max_HP = 80
        self.STR = 20
        self.DEX = 40
        self.equipped_weapon = Bow()
        self.INT = 10
        self.agility = 17
        self.inventory = []
        

class Mage():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Mage"
        self.Def = 15
        self.current_HP = 60
        self.max_HP = 60
        self.STR = 10
        self.DEX = 20
        self.equipped_weapon = Magical_staff()
        self.INT = 50
        self.agility = 12
        self.inventory = [Mana_potion()]
        

class Warrior():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Warrior"
        self.Def = 35
        self.current_HP = 1200
        self.max_HP = 1200
        self.STR = 35
        self.DEX = 35
        self.equipped_weapon = Greatsword()
        self.INT = 20
        self.agility = 12
        self.inventory = []
        

class Gunslinger():
    def __init__(self) -> None:
        self.lvl = 1
        self.klass = "Gunslinger"
        self.Def = 20
        self.current_HP = 90
        self.max_HP = 90        
        self.STR = 15
        self.DEX = 45
        self.equipped_weapon = Tommy_gun()
        self.INT = 10
        self.agility = 20
        self.inventory = []


class Monster():
    def __init__(self, name,lvl, xp,klass,max_HP,current_HP,STR,agility,equipped_weapon):
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.max_HP = max_HP
        self.current_HP = current_HP
        self.STR = STR
        self.agility = agility
        self.inventory = []
        self.klass = klass
        self.equipped_weapon = equipped_weapon
        self.inventory_slots = 1
    
    def __repr__(self) -> None:
        animate_typing (f"""
        {self.name}
        Health:{self.current_HP}/{self.max_HP}
        Level: {self.lvl}
        Strength: {self.STR}
        Speed: {self.agility}
        """)
    
    def take_damage(self, damage):
        self.current_HP = int(self.current_HP - damage)
        return self.current_HP

    def is_dead(self,player):
        if self.current_HP <= 0:
            player.add_xp(self.xp)
            player.add_item(self.inventory)
            animate_typing_slow(f"\n{player.name} landed the final blow and thus the {self.name} has fallen...\n")
            return True
        else:
            return False
    
    def attack(self):
        low_mob_attack_multiplier = random.randint(2,3)
        damage = int((low_mob_attack_multiplier/10) * self.STR)
        return damage

    def enemy_combat_turn(self,player):
        enemy_damage = self.attack()
        player.take_damage(enemy_damage)
        animate_typing(f"\n{self.name} dealt {enemy_damage} damage to you.\n")
        if player.is_dead():
            animate_typing(f"\n{player.name} has been defeated!")


class wolf(Monster):
    def __init__(self):
        super().__init__("Wolf",2,25,"low_Mob",90,90,38,15,None)

class golem(Monster):
    def __init__(self):
        super().__init__("Golem",2,33,"low_Mob",140,140,40,5,"Boulder")

class slime(Monster):
    def __init__(self):
        super().__init__("Slime",1,20,"low_Mob",75,75,35,10,None)

class goblin(Monster):
    def __init__(self):
        super().__init__("Goblin",1,20,"low_Mob",75,75,37,10,"Crooked Knife")

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 3, 35,"low_mob", 100,100, 45, 13,"Two-Handed Axe")

class mountain_Lion(Monster):
    def __init__(self):
        super().__init__("Mountain Lion",2,30,"low_Mob",95,95,40,15,None)

class bats(Monster):
    def __init__(self):
        super().__init__("Bats",1,20,"low_Mob",60,60,35,10,None)

class dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 5, 40,"Mid tier mob", 140,140, 55, 10, None)

class lower_class_demon(Monster):
    def __init__(self) -> None:
        super().__init__("Lower Class Demon",5,37,"Mid tier mob",130,130,53,13,"Longsword of Night and Flame")

class kikimora(Monster):
    def __init__(self):
        super().__init__("Kikimora",5,35,"Mid tier mob",140,140,52,10,None)

class bruxa(Monster):
    def __init__(self):
        super().__init__("Bruxa",6,40,"Mid tier mob",145,145,57,13,None)

class upper_class_demon(Monster):
    def __init__(self) -> None:
        super().__init__("Upper Class Demon",6,42,"Mid tier mob",140,140,60,15,"Moonsword")

class archdemon(Monster):
    def __init__(self):
        super().__init__("Archdemon",8,47,"Boss",170,170,70,15,"Taeshalach the Souleater")

class bevins_bror(Monster):
    def __init__(self):
        super().__init__("Bevins bror",69,666,"Boss",200,200,65,20,"Gaming chair")

class bevins_mamma(Monster):
    def __init__(self):
        super().__init__("Bevins Mamma",666,69420,"The End",420,420,33,6.9,"Child Beater 9000")