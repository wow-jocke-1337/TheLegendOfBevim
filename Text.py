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
        time.sleep(0.00005)
def animate_typing_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

startText = ("""\n
    Welcome to Enter Frozen halls. You found yourself lost inside a dungeon in the mountains 
    and must fight to survive, if you seek to escape and regain your freedom.\n""")

background_info = """
    Developed by three creators, as a school project, the game circles around an action and dungeon-crawler
    type of theme. You start with a goal in mind, meaning mostly linear progression, with side activites also in mind
    and thereby they do not affect the final result."""

inventory_menu = """ 
1 - Use item
2 - Drop item
3 - Go back 

Your choice --> """

combat_options = """
What will you do now?

1 - Attack
2 - Block
3 - Check inventory
4 - Run Away

Your choice --> """

Menu = """ 

    MENU
1 - See stats
2 - Explore
3 - Inventory
4 - See credits
5 - Exit game 


Your choice --> """ #Lägg till Tips & Tricks elr tutorial som beskriver vad saker gör såsom "speed"

door_choice = """
    You have to choose between three doors
    1 - Right
    2 - Forward
    3 - Left
    
    Your choice -->> """

credits = """

    Developers - Balfred, Billiam, Brille bum
    Coders - Balfred, Billiam, Brille bum
    Story writers - Balfred, Billiam, Brille bum
    Art - Balfred, Billiam, Brille bum

"""

prologue_start = """
    You begin your journey through the dark and mysterious corridors of what seems to be a massive structure. The sound of clanking 
    weights banging together, gears circling, heavy chains rattling against each other and several small hisses all together echoing 
    throughout the halls instilling fear into the very moment. However you continue and gradually the noise starts to disappear.   
    """

prologue_end_start ="""\n
    .....A couple of seconds later.....\n"""

prologue_end = """\n
    You are present with.... three choices.\n"""

forest = """
    FFFForest."""

swamp = """
    SSS. Smoking Sexy Style!!!"""

lone_village = """
    Hello Darkness my old friend.""" 

cemetery = """
    You break into an all out fearsome breakdance, with drip practially running off of you, further increasing the feeling of depression by the undead
    and cementing your swagger as unlimited!!!"""

wall_of_spikes_trap = """\nYou recover yourself... However after blowing past you the wall is revealed as able to switch between spikes and having a plain wall 
and its heading back towards you. You feel the largest burst of energy filling you with MOTIVATION and you slash through space and time, destroying the wall in the process.\n\n"""

