import random as rand
from Ascii_Art import*
from Text import *
from Classes import *
from exploring import *
from Rum import *
import random
import os

#Spelar klasser
archer = Archer()
barbarian = Barbarian()
mage = Mage()
warrior = Warrior()
gunslinger = Gunslinger()


#Monster klasserna
wolf_instance = wolf()
goblin_instance = goblin()
orc_instance = Orc()
golem_instance = golem()
slime_instance = slime()
mountain_Lion_instance = mountain_Lion()
bats_instance = bats()
dragon_instance = dragon()
lower_class_demon_instance = lower_class_demon()
upper_class_demon_instance = upper_class_demon()
kikimora_instance = kikimora()
archdemon_instance = archdemon()
bevins_bror_instance = bevins_bror()
bevins_mamma_instance = bevins_mamma()
bruxa_instance = bruxa()

#Rum typerna
room_type = ["M","NA","C","T"]
final_boss_room = ["Morsans_lair"]
M_rooms = ["Bats","Wolf","Golem","Mountain lion","Slime"]
NA_rooms = [forest,swamp,lone_village,cemetery]
C_rooms = ["Treasure room"]
B_rooms = ["Archdemon","Bevins bror","What da hell!"]
T_rooms = ["Pitfall","Wall of spikes","Falling guillotine"]

#De listor monster slumpas från
low_mob_list = [wolf(),golem(),slime(),bats(),mountain_Lion(),Orc(),goblin()]
mid_mob_list = [dragon(),lower_class_demon(),upper_class_demon(), kikimora(),bruxa()]
high_mob_list = [archdemon()]
final_final_boss = [bevins_mamma()]

animate_typing_asciispeed(startText)
time.sleep(1)
print(gameTitle)

time.sleep(2)
animate_typing("What is your name? ")
user_name = input("") 
time.sleep(1)
os.system('cls')

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
        player = Player(user_name, "Barbarian", barbarian.current_HP, barbarian.max_HP, barbarian.lvl,barbarian.Def,barbarian.agility,barbarian.STR,barbarian.DEX,barbarian.equipped_weapon,barbarian.INT,barbarian.inventory)
        os.system('cls')
        break
    elif klass_choice == ARCHER:
        player = Player(user_name, "Archer", archer.current_HP, archer.max_HP, archer.lvl, archer.Def, archer.agility,archer.STR, archer.DEX, archer.equipped_weapon,archer.INT, archer.inventory)
        os.system('cls')
        break
    elif klass_choice == MAGE:
        player = Player(user_name, "Mage", mage.current_HP, mage.max_HP, mage.lvl, mage.Def, mage.agility,mage.STR, mage.DEX, mage.equipped_weapon,mage.INT, mage.inventory)
        os.system('cls')
        break
    elif klass_choice == WARRIOR:
        player = Player(user_name, "Warrior", warrior.current_HP, warrior.max_HP, warrior.lvl, warrior.Def, warrior.agility,warrior.STR, warrior.DEX, warrior.equipped_weapon,warrior.INT, warrior.inventory)
        os.system('cls')
        break
    elif klass_choice == GUNSLINGER:
        player = Player(user_name, "Gunslinger",gunslinger.current_HP, gunslinger.max_HP, gunslinger.lvl, gunslinger.Def, gunslinger.agility, gunslinger.STR, gunslinger.DEX, gunslinger.equipped_weapon,gunslinger.INT, gunslinger.inventory)
        os.system('cls')
        break
    else:
        animate_typing("\n You can only choose between 1-5\n")
        break

player.inventory.append(Healing_potion())
enemy = goblin()

def combat_turn(enemy):
    while True:
    #present combat options to player
        animate_typing(f"""\n{enemy.name} HP: {enemy.current_HP}/{enemy.max_HP}""")
        animate_typing(f"""\n{player.name} HP: {player.current_HP}/{player.max_HP}\n""")
        animate_typing("\nWhat would you like to do?\n1. Attack \n2. Block \n3. Dodge \n4. Use item \n5. Run Away \n\nYour Choice --> ")
        choice = int(input())
        if choice == 1:
            player.player_Attack(enemy)
        elif choice == 2:
            player.block(enemy.attack())
        elif choice == 3:
            player.dodge(enemy)
        elif choice == 4: 
            player.use_item()
        elif choice == 5:
            if player.player_run():
                break
            else:
                continue
        else:
            animate_typing("\nInvalid choice.")
            return True

        if enemy.is_dead():
            animate_typing(f"\n{enemy.name} has been defeated!")
            player.add_xp(enemy.xp)
            return False
        else:
            enemy_damage = enemy.attack()
            player.take_damage(enemy_damage)
            animate_typing(f"\n{enemy.name} dealt {enemy_damage} damage to you.")
            if player.is_dead():
                animate_typing(f"\n{player.name} has been defeated!")
                return False
            return True

def initiate_combat(enemy):
    while True:
        if player.equipped_weapon == None:
            animate_typing(f"\nYou currently do not have a weapon equipped, please equip a weapon from your inventory.")
            player.print_inventory()
            continue
        else:
            if combat_turn(enemy):
                continue
            else:
                break
    return

initiate_combat(enemy)

def gen_room():
    room_count = 0
    if 0 < player.lvl < 9:
            if player.lvl <= 5:
                while True:
                    animate_typing(f"\n{door_choice}")
                    choice_of_door = int(input(""))
                    if choice_of_door == 1 or choice_of_door==2 or choice_of_door==3:
                        room = random.choice(room_type)
                        if room == "M":
                            animate_typing('\nMonster room.\n')
                            monster = random.choice(low_mob_list)
                            # for monster_type in low_mob_list:
                            #     if isinstance(monster,monster_type):
                            #         animate_typing(f"\n You encountered a {monster_type.name}")
                            if isinstance(monster,wolf):
                                animate_typing(f'\nYou encountered a {wolf_instance.name}')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,bats):
                                animate_typing(f'\nYou encountered a {bats_instance.name}!')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,golem):
                                animate_typing(f'\nYou encountered a {golem_instance.name}!')    
                                initiate_combat(monster) 
                                break               
                            elif isinstance(monster,mountain_Lion):
                                animate_typing(f'\nYou encountered a {mountain_Lion_instance.name}!')    
                                initiate_combat(monster) 
                                break              
                            elif isinstance(monster,slime):
                                animate_typing(f'\nYou encountered a {slime_instance.name}!')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,goblin):
                                animate_typing(f'\nYou encountered a {goblin_instance.name}!')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,Orc):
                                animate_typing(f'\nYou encountered a {orc_instance.name}!')
                                initiate_combat(monster)
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
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
            elif player.lvl >= 5:
                while True:
                    animate_typing(f"\n{door_choice}")
                    choice_of_door = int(input(""))
                    if choice_of_door == 1 or choice_of_door==2 or choice_of_door==3:
                        room = random.choice(room_type)
                        if room == "M":
                            animate_typing('\nMonster room.\n')
                            monster = random.choice(mid_mob_list)
                            if isinstance(monster,dragon):
                                animate_typing(f'\nYou encountered a {dragon_instance.name}')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,lower_class_demon):
                                animate_typing(f'\nYou encountered a {lower_class_demon_instance.name}!')
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,upper_class_demon):
                                animate_typing(f'\nYou encountered a {upper_class_demon_instance.name}!')    
                                initiate_combat(monster) 
                                break               
                            elif isinstance(monster,kikimora()):
                                animate_typing(f'\nYou encountered a {kikimora_instance.name}!')    
                                initiate_combat(monster)
                                break               
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
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
            elif player.lvl >= 7:
                while True:
                    animate_typing(f"\n{door_choice}")
                    choice_of_door = int(input(""))
                    if choice_of_door == 1 or choice_of_door==2 or choice_of_door==3:
                        room_type.append("B")
                        room = random.choice(room_type)
                        if room == "M":
                            animate_typing('\nMonster room.\n')
                            monster = random.choice(high_mob_list)
                            if isinstance(monster,archdemon()):
                                animate_typing(f'\nYou encountered a {archdemon_instance.name}')
                                initiate_combat(monster)
                                break
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
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
    elif player.lvl == 9:
        monster = bevins_bror_instance
        animate_typing(f"\nIt is time... To fight your believed to be long lost brother.\n")
        animate_typing(f"\nYou face {bevins_bror_instance.name}, the last gamer to ever grace the earth.\n")
        initiate_combat(monster)
    elif player.lvl == 10:
        monster = bevins_mamma_instance
        animate_typing(f"\n{bevins_mamma_instance.name}")
        initiate_combat(monster)
    else:
        animate_typing(f"""\n\nBruh you go home, you've done enough shitting in this world :|""")
        animate_typing_asciispeed(the_end_of_the_end_end_screen)

time.sleep(1)
animate_typing_slow(f"""

Welcome {player.name} the {player.klass}

""")
time.sleep(1)
def main_menu():
    while True:
        animate_typing(Menu)
        x = int(input(""))
        if x == 1:
            player.print_info()
            time.sleep(2)
        elif x == 2:
            intiate_explore()
            time.sleep(1)
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
        You stopid! Choose an actual alternative, you not dreaming. Because if that were true I would be looking at the summary of your career. 
        You should get a mirror, so you can see how dumb you are. 
        
        /SOme wiSe ASian MAn
        
        """)

main_menu()