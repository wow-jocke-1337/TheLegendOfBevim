from random import randint
import time as sleep
import sys, time


locations = ["Garderoben", "The lair", "Bing bing bang"]
rummet = []
rum = randint(0, 3)

def animate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def gen_room():
    pass

import random

rooms = int(input('How many rooms? : '))
chosen_room = random.randint(1, rooms + 1)
last_room = 'B'

if chosen_room/2 == 0:
    print('M')
elif chosen_room/3 == 0:
    print('F')
elif chosen_room == 3:
    print('K')
    pass
else:
    print('')
