# from random import randint
# from Text import*
# import random as rand
# from combat import*

# room_type = ["M","E","C","B","T"]
# final_boss_room = ["Morsans_lair"]
# M_rooms = ["Bats","Wolf","Golem","Mountain lion","Slime"]
# E_rooms = ["Forest","Swamp","Lone Village","Cemetery"]
# C_rooms = ["Treasure room"]
# B_rooms = ["Archdemon","Bevins bror","What da hell!"]
# T_rooms = ["Pitfall","Wall of spikes","Falling guillotine"]

# def gen_room():
#     room_count = 0
#     if 0 < player.lvl < 9:
#         if player.lvl <= 5:
#             while True:
#                 animate_typing(f"\n{door_choice}")
#                 x = int(input(""))
#                 if x == 1 or x==2 or x==3:
#                     room = random.choice(room_type)
#                     if room == "M":
#                         animate_typing('\nMonster room.')
#                         monster = random.choice(low_mob_list)
#                         if isinstance(monster,wolf):
#                             animate_typing(f'\nYou encountered a {wolf.name}')
#                             initiate_combat()
#                         elif isinstance(monster,bats):
#                             animate_typing(f'\nYou encountered a {bats.name}!')
#                             initiate_combat()
#                         elif isinstance(monster,golem):
#                             animate_typing(f'\nYou encountered a {golem.name}!')    
#                             initiate_combat()                
#                         elif isinstance(monster,mountain_Lion):
#                             animate_typing(f'\nYou encountered a {mountain_Lion.name}!')    
#                             initiate_combat()               
#                         elif isinstance(monster,slime):
#                             animate_typing(f'\nYou encountered a {slime.name}!')
#                             initiate_combat()
#                         elif isinstance(monster,goblin):
#                             animate_typing(f'\nYou encountered a {goblin.name}!')
#                             initiate_combat()
#                     elif room == "E":
#                         animate_typing(f'\nThis room is empty.')
#                     elif room == "C":
#                         animate_typing(f'\nYou found a Treasure!')
#                     elif room == "T":
#                         animate_typing(f'\nTrap room.\n')
#                         trap = random.choice(T_rooms)
#                         if trap == "Pitfall":
#                             animate_typing(f'\nYou fell!')
#                         elif trap == "Moving Wall of spikes":
#                             animate_typing(f'\nYou got spiked and lost hp!\n')
#                             animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
#                             and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
#                         else:
#                             animate_typing('\nSevered you are!')
#                     room_count += 1
#                     animate_typing(f"""\n
#                     Amount of rooms completed: {room_count}
#                     """)
#                 else:
#                     animate_typing("\nStoooopid!")
#         elif Player.lvl >= 5:
#             while True:
#                 animate_typing(f"\n{door_choice}")
#                 x = int(input(""))
#                 if x == 1 or x==2 or x==3:
#                     room = random.choice(room_type)
#                     if room == "M":
#                         animate_typing('\nMonster room.')
#                         monster = random.choice(mid_mob_list)
#                         if isinstance(monster,dragon):
#                             animate_typing(f'\nYou encountered a {dragon.name}')
#                             initiate_combat()
#                         elif isinstance(monster,lower_class_demon):
#                             animate_typing(f'\nYou encountered a {lower_class_demon.name}!')
#                             initiate_combat()
#                         elif isinstance(monster,upper_class_demon):
#                             animate_typing(f'\nYou encountered a {upper_class_demon.name}!')    
#                             initiate_combat()                
#                         elif isinstance(monster,kikimora()):
#                             animate_typing(f'\nYou encountered a {kikimora.name}!')    
#                             initiate_combat()               
#                     elif room == "E":
#                         animate_typing('\nThis room is empty.')
#                     elif room == "C":
#                         animate_typing('\nYou found a Treasure!')
#                     elif room == "T":
#                         animate_typing('\nTrap room.\n')
#                         trap = random.choice(T_rooms)
#                         if trap == "Pitfall":
#                             animate_typing('\nYou fell!')
#                         elif trap == "Moving Wall of spikes":
#                             animate_typing(f'\nYou got spiked and lost hp!\n')
#                             animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
#                             and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
#                         else:
#                             animate_typing('\nSevered you are!')
#                 else:
#                     animate_typing("\nStoooopid!")
#         elif Player.lvl >= 7:
#             while True:
#                 animate_typing(f"\n{door_choice}")
#                 x = int(input(""))
#                 if x == 1 or x==2 or x==3:
#                     room = random.choice(room_type)
#                     if room == "M":
#                         animate_typing('\nMonster room.')
#                         monster = random.choice(high_mob_list)
#                         if isinstance(monster,archdemon()):
#                             animate_typing(f'\nYou encountered a {archdemon.name}')
#                             initiate_combat()
#                     elif room == "E":
#                         animate_typing('\nThis room is empty.')
#                     elif room == "C":
#                         animate_typing('\nYou found a Treasure!')
#                     elif room == "T":
#                         animate_typing('\nTrap room.\n')
#                         trap = random.choice(T_rooms)
#                         if trap == "Pitfall":
#                             animate_typing('\nYou fell!')
#                         elif trap == "Moving Wall of spikes":
#                             animate_typing(f'\nYou got spiked and lost hp!\n')
#                             animate_typing(f"""\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
#                             and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n""")
#                         else:
#                             animate_typing('\nSevered you are!')
#                 else:
#                     animate_typing("\nStoooopid!")   
#     elif Player.lvl == 9:
#         animate_typing(f"\nIt is time... To fight your believed to be long lost brother.\n")
#         animate_typing(f"\nYou face X, the last gamer to ever grace the earth.\n")
#         Player.start_combat(bevins_bror())
#     else:
#         animate_typing(f"\n{bevins_mamma}")