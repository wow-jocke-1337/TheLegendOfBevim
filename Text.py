from time import sleep
import sys,time,random

def animate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def animate_typing_asciispeed(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0)

def animate_typing_fast(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

startText = ("""
Welcome to _! You found yourself lost inside a dungeon in the mountains, a strange aura radiates from the walls turning your legs to jelly, 
a knot forms inside of you, telling you to run. However you simply continue staying in your place, planted in place. 
To escape from this hellhole """)

Menu = """ 

    MENU
1 - see stats
2 -
3 - Exit game


Your choice --> """
