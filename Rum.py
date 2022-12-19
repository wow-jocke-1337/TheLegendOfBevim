from random import randint
from Text import*

def gen_room():
    pass

import random as rand

boss_room = ["Morsans Lair"]
chest_rooms = ["Windstrucken Barn ", "A Nesting site ", "Valley ", "Volcanic Caverns ", "Skyisland ", "Duskwoods ", "Graveyard ", "Niagara Falls ", "Ivory Tower ", "Bing bing bang "]
starting_room = []
monster_room = []
trap_room = []
chosen_room = []
#Start rummet är alltid lika med 0. Start rummet ska poppas ur listan i början.
#Resten av rummen ska få slumpade värden varje gång. 

if "Windstrucken Barn " in chest_rooms:
    starting_room.extend(chest_rooms[0])
    chest_rooms.pop(0)
    animate_typing("""\n
    You arrive at a Windstrucken Barn, looking around you find that the barn is abandoned and the cause of your arrival seems at first a mystery.
    Collecting yourself, you search the barn discovering nothing but that the light is out of reach, wherever you are this place does not come of as
    merciful, but cursed and ancient in some way. 
        Survive and successfully escape, but first you must choose one of the three doors currently infront of you.""")
    time.sleep(1)
    animate_typing("""\n
    1: Right?
    2: Middle?
    3: Left? 
        """)
