from random import randint
from Text import*
import random as rand

room_type = ["M","E","C","B","T"]
final_boss_room = ["Morsans lair"]
M_rooms = ["Bats","Wolf","Golem","Mountain lion","Slime"]
E_rooms = ["Forest","Swamp","Lone Village","Cemetery"]
C_rooms = ["Treasure room"]
B_rooms = ["Archdemon","Bevins bror","What da hell!",""]
T_rooms = ["Pitfall","Wall of spikes","Falling guillotine"]

def gen_room():
    room = random.choice(room_type)
    if room == "M":
        animate_typing('\nMonster room.')
        monster = random.choice(M_rooms)
        if monster == "Bats":
            animate_typing('\nYou encountered a pack of bats!')
        elif monster == "Wolf":
            animate_typing('\nYou encountered a Wolf!')
        elif monster == "Golem":
            animate_typing('\nYou encountered a Golem!')
        elif monster == "Mountain lion":
            animate_typing('\nYou encountered a Mountain lion!')
        elif monster == "Slime":
            animate_typing('\nYou encountered a slime!')
    elif room == "E":
        animate_typing('\nThis room is empty.')
    elif room == "C":
        animate_typing('\nYou found a Treasure!')
    elif room == "B":
        animate_typing('\nBoss room.')
        boss = random.choice(B_rooms)
        if boss == "Archdemon":
            animate_typing('\nYou encountered a Archdemon!')
        elif boss == "Bevins bror":
            animate_typing('\nYou encountered your brother, Bing CHilling!')
        else:
            animate_typing('\nWhat da hell!')
    elif room == "T":
        animate_typing('\nTrap room.')
        trap = random.choice(T_rooms)
        if trap == "Pitfall":
            animate_typing('\nYou fell!')
        elif trap == "Wall of spikes":
            animate_typing('\nYou got spiked!')
        else:
            animate_typing('\nSevered you are!')
    

def room_count():
    pass