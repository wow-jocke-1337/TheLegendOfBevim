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
bevin_himself = Bevin_himself()

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

#Olika Vapen
greatsword_instance = Greatsword()
magical_staff_instance = Magical_staff()
axe_instance = Axe()
bow_instance = Bow()
tommy_gun_instance = Tommy_gun()
moonlight_greatsword_instance = Moonlight_greatsword()

item_list = [greatsword_instance, magical_staff_instance, axe_instance, bow_instance, tommy_gun_instance,moonlight_greatsword_instance]

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
endgame_mob_list = [archdemon()]
final_final_boss = [bevins_mamma()]


animate_typing_asciispeed(gameTitle)
time.sleep(4)
animate_typing(startText)
time.sleep(2)
os.system('cls')
animate_typing("What is thou called? ")
user_name = input("")
os.system('cls')
if user_name == "Bevin" or "Alfred" or "Krille" or "William" or "Bing":
    animate_typing_slow("\n\nA real fine name indeed. ")
    animate_typing_slow("Although great names often signify the art of a great passing, let us hope thou shalt not falter as the others did.....")
time.sleep(2)
os.system('cls')

while True:
    animate_typing("""

    Kindly choose thy class. 
        
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
    BEVINHIMSELF = "666"
    
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
    elif klass_choice == BEVINHIMSELF:
        player = Player(user_name, "Bevin Himself",bevin_himself.current_HP, bevin_himself.max_HP, bevin_himself.lvl, bevin_himself.Def, bevin_himself.agility, bevin_himself.STR, bevin_himself.DEX, bevin_himself.equipped_weapon,bevin_himself.INT, bevin_himself.inventory)
        os.system('cls')
        break
    else:
        animate_typing("\n You can only choose between 1-6\n")
        os.system('cls')
player.inventory.append(Healing_potion())
time.sleep(2)
animate_typing_slow(f"""

Welcome {player.name} the {player.klass}

""")
time.sleep(1.5)
os.system('cls')
def main_menu():
    while True:
        animate_typing(Menu)
        x = int(input(""))
        if x == 1:
            os.system('cls')
            player.print_info()
            time.sleep(3)
            os.system('cls')
        elif x == 2:
            if player.XP > 0:
                os.system('cls')
                time.sleep(1)
                gen_room()
                time.sleep(1)
            else:
                os.system('cls')
                intiate_first_explore()
                time.sleep(1)
                os.system('cls')
                gen_room()
                time.sleep(1)
        elif x == 3:
            os.system('cls')
            player.print_inventory()
            time.sleep(2)
            os.system('cls')
        elif x == 4:
            os.system('cls')
            animate_typing(credits)
            time.sleep(2)
        elif x == 5:
            os.system('cls')
            animate_typing("""
        Thank you for playing :) 

        """)
            exit()
        else:
            os.system('cls')
            animate_typing("""
        You stopid! Choose an actual alternative, you not dreaming. Because if that were true I would be looking at the summary of your career. 
        You should get a mirror, so you can see how dumb you are. 
        
        /SOme wiSe ASian MAn
        
        """)

def combat_turn(enemy):
    while True:
    #present combat options to player
        if enemy.is_dead(player):
            os.system('cls')
            break
        else:
            animate_typing(f"""\n{enemy.name} HP: {enemy.current_HP}/{enemy.max_HP}""")
            animate_typing(f"""\n{player.name} HP: {player.current_HP}/{player.max_HP}\n""")
            animate_typing("\nWhat would you like to do?\n1. Attack \n2. Block \n3. Dodge \n4. Use item \n5. Run Away \n\nYour Choice --> ")
            choice = int(input())
            if choice == 1:
                os.system('cls')
                player.player_Attack(enemy)
                enemy.enemy_combat_turn(player)
            elif choice == 2:
                os.system('cls')
                player.block(enemy.attack())
            elif choice == 3:
                os.system('cls')
                if player.dodge(enemy):
                    animate_typing(f"\n{player.name} successfully dodged their attack.\n")
                else:
                    animate_typing(f"\n{player.name} was to slow to dodge the attack.\n")
                    enemy.enemy_combat_turn(player)
            elif choice == 4:
                os.system('cls')
                player.print_inventory()
            elif choice == 5:
                os.system('cls')
                if player.player_run():
                    break
                else:
                    continue
            else:
                os.system('cls')
                animate_typing("\nInvalid choice.")
                return True

def initiate_combat(enemy):
    while True:
        if player.equipped_weapon == None:
            animate_typing(f"\nYou currently do not have a weapon equipped, please equip a weapon from your inventory.")
            os.system('cls')
            player.print_inventory()
            continue
        else:
            if combat_turn(enemy):
                continue
            else:
                break
    return

def gen_room():
    room_count = 0
    if 0 < player.lvl < 9:
            if player.lvl <= 5:
                while True:
                    animate_typing(f"\n{door_choice}")
                    choice_of_door = int(input(""))
                    if choice_of_door == 1 or choice_of_door==2 or choice_of_door==3:
                        room = random.choice(room_type)
                        os.system('cls')
                        if room == "M":
                            animate_typing('\nMonster room.\n')
                            monster = random.choice(low_mob_list)
                            # for monster_type in low_mob_list:
                            #     if isinstance(monster,monster_type):
                            #         animate_typing(f"\n You encountered a {monster_type.name}")
                            if isinstance(monster,wolf):
                                animate_typing(f'\nYou encountered a {wolf_instance.name}\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,bats):
                                animate_typing(f'\nYou encountered {bats_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,golem):
                                animate_typing(f'\nYou encountered a {golem_instance.name}!\n') 
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)   
                                initiate_combat(monster) 
                                break               
                            elif isinstance(monster,mountain_Lion):
                                animate_typing(f'\nYou encountered a {mountain_Lion_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)    
                                initiate_combat(monster) 
                                break              
                            elif isinstance(monster,slime):
                                animate_typing(f'\nYou encountered a {slime_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,goblin):
                                animate_typing(f'\nYou encountered a {goblin_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,Orc):
                                animate_typing(f'\nYou encountered an {orc_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
                        elif room == "C":
                            found_item = random.choice(item_list)
                            player.add_item(found_item)
                            animate_typing(f'\nYou found a {found_item.name}!\n')
                        elif room == "T":
                            animate_typing(f'\nTrap room.\n')
                            trap = random.choice(T_rooms)
                            if trap == "Pitfall":
                                animate_typing(f'\nYou fell!\n')
                            elif trap == "Moving Wall of spikes":
                                animate_typing(wall_of_spikes_trap)
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
                                animate_typing(f'\nYou encountered a {dragon_instance.name}\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,lower_class_demon):
                                animate_typing(f'\nYou encountered a {lower_class_demon_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                            elif isinstance(monster,upper_class_demon):
                                animate_typing(f'\nYou encountered an {upper_class_demon_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)    
                                initiate_combat(monster) 
                                break               
                            elif isinstance(monster,kikimora):
                                animate_typing(f'\nYou encountered a {kikimora_instance.name}!\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)    
                                initiate_combat(monster)
                                break               
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
                        elif room == "C":
                            found_item = random.choice(item_list)
                            player.add_item(found_item)
                            animate_typing(f'\nYou found a {found_item.name}!\n')
                        elif room == "T":
                            animate_typing('\nTrap room.\n')
                            trap = random.choice(T_rooms)
                            if trap == "Pitfall":
                                animate_typing('\nYou fell!\n')
                            elif trap == "Moving Wall of spikes":
                                animate_typing(wall_of_spikes_trap)
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
                            monster = random.choice(endgame_mob_list)
                            if isinstance(monster,archdemon):
                                animate_typing(f'\nYou encountered an {archdemon_instance.name}\n')
                                monster_item = random.choice(item_list)
                                monster.inventory.append(monster_item)
                                initiate_combat(monster)
                                break
                        elif room == "NA":
                            new_area = random.choice(NA_rooms)
                            animate_typing(new_area)
                        elif room == "C":
                            found_item = random.choice(item_list)
                            player.add_item(found_item)
                            animate_typing(f'\nYou found a {found_item.name}!\n')
                        elif room == "T":
                            animate_typing('\nTrap room.\n')
                            trap = random.choice(T_rooms)
                            if trap == "Pitfall":
                                animate_typing('\nYou fell!')
                            elif trap == "Moving Wall of spikes":
                                animate_typing(f'\nYou got spiked and lost hp!\n')
                                animate_typing(wall_of_spikes_trap)
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
        exit()

main_menu()