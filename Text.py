from time import sleep
import random as rand
import time
import sys,time,random

def animate_typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

class Player():
    
    def __init__(self, klass, lifes, capacity, armor):
        self.lifes = lifes
        self.scores = 0
        self.armor = armor
        self.did_hit = False
        self.is_hitted = False
        self.capacity = capacity
        self.klass = klass

    def print_info(self):
        animate_typing(f"""
                Character: {self.klass}
                Health: {self.lifes}/{self.lifes} Armour: {self.armor}/{self.armor} 
                Capacity: {self.capacity}/{self.capacity+5}""") 

    def fire(self):
        pass
       # Här sker "eldväxlingen"

    def inc_scores(self): 
        pass
       # Här ska poängen öka

    def get_shot(self):
        pass
        # Här ska antalet liv minska
def begin():
    print(f"""
     _________  ___  ___  _______           ________  _______   ___      ___ _______   ________   ________  _______           ________  ___________ 
    |\___   ___\|  \|\  \|\  ___ \         |\   __  \|\  ___ \ |\  \    /  /|\  ___ \ |\   ___  \|\   ____\|\  ___ \         |\   __  \|\  _______/
    \|___ \  \_\ \  \|\  \ \   __/|        \ \  \|\  \ \   __/|\ \  \  /  / | \   __/|\ \  | \  \ \  \___|\ \   __/|         \ \  \ \  \ \  \____/ 
         \ \  \ \ \   __  \ \  \_|/__       \ \   _  _\ \  \_|/_\ \  \/  / / \ \  \_|/_\ \  | \  \ \  \  __\ \  \_|/__        \ \  \ \  \ \   ___/
          \ \  \ \ \  \ \  \ \  \_|\ \       \ \  |\   \ \  \_|\ \ \    / /   \ \  \_|\ \ \  |\ \  \ \  \|\ \ \  \_|\ \        \ \  \_\  \ \  \_/
           \ \__\ \ \__\ \__\ \_______\       \ \__|\ _ \ \_______\ \__/ /     \ \_______\ \__|\ \__\ \______\ \_______\        \ \_______\ \__|
            \|__|  \|__|\|__|\|_______|        \|__|\|__|\|_______|\|__|/       \|_______|\|__| \|__|\|______|\|_______|         \|_______|\|__| 
                                                                                                                                             
                                                                                                                                             
                                                                                                                                             
     ________  _______   ___      ___ ___  _____ ______   ________           _____ ______   ________  ________  ________  ________               
    |\   __  \|\  ___ \ |\  \    /  /|\  \|\   _ \  _   \|\   ____\         |\   _ \  _   \|\   __  \|\   __  \|\   ____\|\   __  \              
    \ \  \|\ /\ \   __/|\ \  \  /  / | \  \ \  \ \__\ \  \ \  \___|_        \ \  \ \__\ \  \ \  \ \  \ \  \ \  \ \  \___|\ \  \ \  \             
     \ \   __  \ \  \_|/_\ \  \/  / / \ \  \ \  \_|__| \  \ \_____  \        \ \  \_|__| \  \ \  \ \  \ \   _  _\ \_____  \ \   __  \            
      \ \  \|\  \ \  \_|\ \ \    / /   \ \  \ \  \    \ \  \|____|\  \        \ \  \    \ \  \ \  \ \  \ \  |\  \|_____|\  \ \  \ \  \           
       \ \_______\ \_______\ \__/ /     \ \__\ \__\    \ \__\____\_\  \        \ \__\    \ \__\ \_______\ \__|\ _\ ____\_\  \ \__\ \__\          
        \|_______|\|_______|\|__|/       \|__|\|__|     \|__|\_________\        \|__|     \|__|\|_______|\|__|\|__|\_________\|__|\|__|          
                                                            \|_________|                                          \|_________|                   
                                                                                                                                             """) 
    
    animate_typing("""\nVälkommen till vårt spel! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
begin()
player_one = Player("Bevim", 100, 0, 0)
player_one.print_info()