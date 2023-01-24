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
def animate_typing_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

startText = ("""
    Welcome to The Tales of an Adventurer. You found yourself lost inside a dungeon in the mountains 
    and must fight to survive, if you seek to escape and regain your freedom.""")

background_info = """
    Developed by three creators, as a school project, the game circles around an action and dungeon-crawler
    type of theme. You start with a goal in mind, meaning mostly linear progression, with side activites also in mind
    and thereby they do not affect the final result."""

inventory_menu = """ 
1 - Use item
2 - Drop item
3 - Go back 

Your choice --> """



credits = """

Developers - Balfred, Billiam, Brille bum
Coders - Balfred, Billiam, Brille bum
Story writers - Balfred, Billiam, Brille bum
Art - Balfred, Billiam, Brille bum

"""

prologue_start = """
    You begin your journey through the dark and mysterious corridors of what seems to be a massive structure. The sound of clanking 
    weights banging together, gears circling, heavy chains rattling against each other and several small hisses all together echoing 
    throughout the halls instilling fear into the very moment. However you continue and the noise    
    """

prologue_end_start = """
    .....A couple of seconds later....."""

prologue_end = """
    You are present with """