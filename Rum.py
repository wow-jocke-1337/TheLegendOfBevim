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
    
