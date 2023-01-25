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

room_type = ["M","E","C","B","T"]
final_boss_room = ["Morsans_lair"]
M_rooms = ["Bats","Wolf","Golem","Mountain lion","Slime"]
E_rooms = ["Forest","Swamp","Lone Village","Cemetery"]
C_rooms = ["Treasure room"]
B_rooms = ["Archdemon","Bevins bror","What da hell!"]
T_rooms = ["Pitfall","Wall of spikes","Falling guillotine"]

low_mob_list = [wolf(),golem(),slime(),bats(),mountain_Lion(),Orc()]
mid_mob_list = [dragon(),lower_class_demon(),upper_class_demon(), kikimora()]
high_mob_list = [archdemon()]
final_boss = [bevins_mamma()]


def attack():
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3 or 4:
            animate_typing("\nYou hit the target!")
            damage()
        else:
            animate_typing("\nYou missed.")

def block():
        outcome=random.choice(list)
        if outcome==1 or outcome==2 or outcome==3:
            animate_typing("\nSuccessfully blocked!")
        else:
            animate_typing("\nyou failed to block and took damage!"  + {player.STR} *0.25)


def Exit_Combat(): 
        outcome= random.choice(list)
        if outcome== 1 or 2:
            animate_typing("\nSuccess! You ran away")
        else:
            animate_typing("\You Failed to Run Away!")

def combat_choices():
    while True:
        animate_typing(combat_options)
        x=int(input("")) 
        if x==1: 
            attack()
            break
        elif x==2:
            block()
            break
        elif x==3:
            player.print_inventory()
            break
        elif x==4:
            animate_typing(f"\nYou Died")
            exit()
        else:
            animate_typing(f"\nChoose one of the alternatives.")
            break

def damage():
    while True:
        outcome=random.choice(list)
        if outcome== 1 or 2 or 3:
            dmg =  player.calculate_damage()
            animate_typing(f"\nYou dealt {dmg} hitpoints.")
            break
        else:
            animate_typing(f"\n\nYou dealt no damage.")
            break

          
def Game_over():
    if player.HP > 50:
        animate_typing("HP is at a stable level")
        if 35 > player.HP > 20:
            animate_typing("You need to heal, HP is at a low level!")
    if player.HP <=0:
        animate_typing("You got killed by the monster!")
        exit()

  
def initiate_combat():
    if player.equipped_weapon == None:
        animate_typing(f"""\nYou currently do not have a weapon equipped, thereby giving you no chance in a fight.""")
        player.print_inventory()
    combat_choices()

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
        player = Player(user_name, "Barbarian", barbarian.HP, barbarian.Def, barbarian.spd,barbarian.lvl,barbarian.STR, barbarian.DEX, barbarian.INT, barbarian.inventory)
        player.inventory.append(Axe())
        break
    elif klass_choice == ARCHER:
        player = Player(user_name, "Archer", archer.HP, archer.Def, archer.spd, archer.lvl,archer.STR, archer.DEX, archer.INT, archer.inventory)
        player.inventory.append(Bow())
        break
    elif klass_choice == MAGE:
        player = Player(user_name, "Mage", mage.HP, mage.Def, mage.spd, mage.lvl,mage.STR, mage.DEX, mage.INT, mage.inventory)
        player.inventory.append(Mana_potion())
        player.inventory.append(Magical_staff())
        break
    elif klass_choice == WARRIOR:
        player = Player(user_name, "Warrior", warrior.HP,warrior.Def, warrior.spd, warrior.lvl,warrior.STR, warrior.DEX, warrior.INT, warrior.inventory)
        player.inventory.append(Greatsword())
        break
    elif klass_choice == GUNSLINGER:
        player = Player(user_name, "Gunslinger", gunslinger.HP, gunslinger.Def, gunslinger.spd, gunslinger.lvl,gunslinger.DEX, gunslinger.INT, gunslinger.STR, gunslinger.inventory)
        player.inventory.append(Tommy_gun())
        break
    else:
        animate_typing("\n You can only choose between 1-5\n")
        break

player.inventory.append(Healing_potion())

def gen_room():
    room_count = 0
    if 0 < player.lvl < 9:
        if self.lvl <= 5:
            while True:
                animate_typing(f"\n{door_choice}")
                x = int(input(""))
                if x == 1 or x==2 or x==3:
                    room = random.choice(room_type)
                    if room == "M":
                        animate_typing('\nMonster room.')
                        monster = random.choice(low_mob_list)
                        if isinstance(monster,wolf):
                            animate_typing(f'\nYou encountered a {wolf.name}')
                            initiate_combat()
                        elif isinstance(monster,bats):
                            animate_typing(f'\nYou encountered a {bats.name}!')
                            initiate_combat()
                        elif isinstance(monster,golem):
                            animate_typing(f'\nYou encountered a {golem.name}!')    
                            initiate_combat()                
                        elif isinstance(monster,mountain_Lion):
                            animate_typing(f'\nYou encountered a {mountain_Lion.name}!')    
                            initiate_combat()               
                        elif isinstance(monster,slime):
                            animate_typing(f'\nYou encountered a {slime.name}!')
                            initiate_combat()
                        elif isinstance(monster,goblin):
                            animate_typing(f'\nYou encountered a {goblin.name}!')
                            initiate_combat()
                    elif room == "E":
                        animate_typing(f'\nThis room is empty.')
                    elif room == "C":
                        animate_typing(f'\nYou found a Treasure!')
                    elif room == "T":
                        animate_typing(f'\nTrap room.\n')
                        trap = random.choice(T_rooms)
                        if trap == "Pitfall":
                            animate_typing(f'\nYou fell!')
                        elif trap == "Moving Wall of spikes":
                            animate_typing(f'\nYou got spiked and lost hp!\n')
                            animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
                            and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
                        else:
                            animate_typing('\nSevered you are!')
                    room_count += 1
                    animate_typing(f"""\n
                    Amount of rooms completed: {room_count}
                    """)
                else:
                    animate_typing("\nStoooopid!")
        elif self.lvl >= 5:
            while True:
                animate_typing(f"\n{door_choice}")
                x = int(input(""))
                if x == 1 or x==2 or x==3:
                    room = random.choice(room_type)
                    if room == "M":
                        animate_typing('\nMonster room.')
                        monster = random.choice(mid_mob_list)
                        if isinstance(monster,dragon):
                            animate_typing(f'\nYou encountered a {dragon.name}')
                            initiate_combat()
                        elif isinstance(monster,lower_class_demon):
                            animate_typing(f'\nYou encountered a {lower_class_demon.name}!')
                            initiate_combat()
                        elif isinstance(monster,upper_class_demon):
                            animate_typing(f'\nYou encountered a {upper_class_demon.name}!')    
                            initiate_combat()                
                        elif isinstance(monster,kikimora()):
                            animate_typing(f'\nYou encountered a {kikimora.name}!')    
                            initiate_combat()               
                    elif room == "E":
                        animate_typing('\nThis room is empty.')
                    elif room == "C":
                        animate_typing('\nYou found a Treasure!')
                    elif room == "T":
                        animate_typing('\nTrap room.\n')
                        trap = random.choice(T_rooms)
                        if trap == "Pitfall":
                            animate_typing('\nYou fell!')
                        elif trap == "Moving Wall of spikes":
                            animate_typing(f'\nYou got spiked and lost hp!\n')
                            animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
                            and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
                        else:
                            animate_typing('\nSevered you are!')
                else:
                    animate_typing("\nStoooopid!")
        elif self.lvl >= 7:
            while True:
                animate_typing(f"\n{door_choice}")
                x = int(input(""))
                if x == 1 or x==2 or x==3:
                    room = random.choice(room_type)
                    if room == "M":
                        animate_typing('\nMonster room.')
                        monster = random.choice(high_mob_list)
                        if isinstance(monster,archdemon()):
                            animate_typing(f'\nYou encountered a {archdemon.name}')
                            initiate_combat()
                    elif room == "E":
                        animate_typing('\nThis room is empty.')
                    elif room == "C":
                        animate_typing('\nYou found a Treasure!')
                    elif room == "T":
                        animate_typing('\nTrap room.\n')
                        trap = random.choice(T_rooms)
                        if trap == "Pitfall":
                            animate_typing('\nYou fell!')
                        elif trap == "Moving Wall of spikes":
                            animate_typing(f'\nYou got spiked and lost hp!\n')
                            animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
                            and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
                        else:
                            animate_typing('\nSevered you are!')
                else:
                    animate_typing("\nStoooopid!")   
    elif self.lvl == 9:
        animate_typing(f"\nIt is time... To fight your believed to be long lost brother.\n")
        animate_typing(f"\nYou face X, the last gamer to ever grace the earth.\n")
        initiate_combat()
    elif self.lvl == 10:
        animate_typing(f"\n{bevins_mamma}")

def attack():
        outcome = random.choice(list)
        if outcome == 1 or 2 or 3 or 4:
            animate_typing("\nYou hit the target!")
            damage()
        else:
            animate_typing("\nYou missed.")

def block():
        outcome=random.choice(list)
        if outcome==1 or outcome==2 or outcome==3:
            animate_typing("\nSuccessfully blocked!")
        else:
            animate_typing("\nyou failed to block and took damage!"  + {player.STR} *0.25)


def Exit_Combat(): 
        outcome= random.choice(list)
        if outcome== 1 or 2:
            animate_typing("\nSuccess! You ran away")
        else:
            animate_typing("\You Failed to Run Away!")

def combat_choices():
    while True:
        animate_typing(combat_options)
        x=int(input("")) 
        if x==1: 
            attack()
            break
        elif x==2:
            block()
            break
        elif x==3:
            player.print_inventory()
            break
        elif x==4:
            animate_typing(f"\nYou Died")
            exit()
        else:
            animate_typing(f"\nChoose one of the alternatives.")
            break

def damage():
    while True:
        outcome=random.choice(list)
        if outcome== 1 or 2 or 3:
            dmg =  player.calculate_damage()
            animate_typing(f"\nYou dealt {dmg} hitpoints.")
            break
        else:
            animate_typing(f"\n\nYou dealt no damage.")
            break

          
def Game_over():
    if player.HP > 50:
        animate_typing("HP is at a stable level")
        if 35 > player.HP > 20:
            animate_typing("You need to heal, HP is at a low level!")
    if player.HP <=0:
        animate_typing("You got killed by the monster!")
        exit()

  
def initiate_combat():
    if player.equipped_weapon == None:
        animate_typing(f"""\nYou currently do not have a weapon equipped, thereby giving you no chance in a fight.""")
        player.print_inventory()
    combat_choices()


time.sleep(1)
animate_typing_slow(f"""

Welcome {player.name} the {player.klass}

""")


time.sleep(1)

while True:
    animate_typing(Menu)
    x = int(input(""))
    if x == 1:
        player.print_info()
        time.sleep(2)
    elif x == 2:
        intiate_explore()
        gen_room()
        time.sleep(1) 
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