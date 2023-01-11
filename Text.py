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
    Welcome to The Tales of an Adventurer. You found yourself lost inside a dungeon in the mountains 
    and must fight to survive, if you seek to escape and regain your freedom.""")

background_info = """
    Developed by three creators, as a school project, the game circles around an action and dungeon-crawler
    type of theme. You start with a goal in mind, meaning mostly linear progression, with side activites also in mind
    and thereby they do not affect the final result."""

credits = """

Developers - Balfred, Billiam, Brille bum
Coders - Balfred, Billiam, Brille bum
Story writers - Balfred, Billiam, Brille bum
Art - Balfred, Billiam, Brille bum

"""

