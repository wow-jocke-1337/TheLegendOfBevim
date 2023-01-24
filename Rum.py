from random import randint
from Text import*
import random as rand
from combat import*

room_type = ["M","E","C","B","T"]
final_boss_room = ["Morsans_lair"]
M_rooms = ["Bats","Wolf","Golem","Mountain lion","Slime"]
E_rooms = ["Forest","Swamp","Lone Village","Cemetery"]
C_rooms = ["Treasure room"]
B_rooms = ["Archdemon","Bevins bror","What da hell!"]
T_rooms = ["Pitfall","Wall of spikes","Falling guillotine"]

def gen_room():
    door_choice = """
    You have to choose between three doors
    1 - Right
    2 - Forward
    3 - Left
    
    Your choice -->> """
    room_count = 0
    if Player.lvl < 9:
        while True:
            animate_typing(f"\n{door_choice}")
            x = int(input(""))
            if x == 1 or x==2 or x==3:
                room = random.choice(room_type)
                if room == "M":
                    animate_typing('\nMonster room.')
                    monster = random.choice(low_mob_list)
                    if isinstance(monster,wolf):
                        animate_typing('\nYou encountered a Wolf')
                        initiate_combat()
                    elif isinstance(monster,bats):
                        animate_typing('\nYou encountered a pack of Bats!')
                        initiate_combat()
                    elif isinstance(monster,golem):
                        animate_typing('\nYou encountered a Golem!')    
                        initiate_combat()                
                    elif isinstance(monster,mountain_Lion):
                        animate_typing('\nYou encountered a Mountain lion!')    
                        initiate_combat()               
                    elif isinstance(monster,slime):
                        animate_typing('\nYou encountered a slime!')
                        initiate_combat()
                    elif isinstance(monster,goblin):
                        animate_typing('\nYou encountered a goblin!')
                        initiate_combat()
                elif room == "E":
                    animate_typing('\nThis room is empty.')
                elif room == "C":
                    animate_typing('\nYou found a Treasure!')
                elif room == "B":
                    animate_typing('\nBoss room.')
                    boss = random.choice(high_mob_list)
                    if isinstance(monster,archdemon):
                        animate_typing('\nYou encountered a Archdemon')
                        initiate_combat()                   
                    elif boss == "Bevins bror":
                        animate_typing('\nYou encountered your brother, Bing CHilling!\n')
                        initiate_combat()
                    elif isinstance(monster,wolf):
                        animate_typing('\nYou encountered a Wolf')
                        initiate_combat()
                elif room == "T":
                    animate_typing('\nTrap room.\n')
                    trap = random.choice(T_rooms)
                    if trap == "Pitfall":
                        animate_typing('\nYou fell!')
                    elif trap == "Moving Wall of spikes":
                        animate_typing(f'\nYou got spiked and lost {Player.HP * 0.1} hp!\n')
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
    
    elif Player.lvl == 9:
        animate_typing(f"\nIt is time... To fight your believed to be long lost brother.\n")
        animate_typing(f"\nYou face X, the last gamer to ever grace the earth.\n")
        initiate_combat(bevins_bror())
    else:
        exit()