from random import randint
import time as sleep
import sys, time

def animate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def gen_room():
    pass

import random as rand

rooms = ["Windstrucken Barn ", "A Nesting site ", "Valley ", "Volcanic Caverns ", "Skyisland ", "Duskwoods ", "Graveyard ", "Niagara Falls ", "Ivory Tower ", "Bing bing bang "]
starting_room = []
chosen_rooms = []
#Start rummet är alltid lika med 0. Start rummet ska poppas ur listan i början.
#Resten av rummen ska få slumpade värden varje gång. 

if "Windstrucken Barn " in rooms:
    starting_room.extend(rooms[0])
    rooms.pop(0)
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