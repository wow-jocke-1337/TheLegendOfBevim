import time as sleep
import sys, time

class Player():
    def info(self, name, HP):
        self.name = name
        self.lvl = 0
        self.did_hit = False
        self.is_hitted = False

    def animate_typing(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

    def print_info(self, Class):

        print(f""" 
        {Player.name}
        LVL: {Player.lvl} 
        HP: {Player.HP}

        
        """)

    def attack():
        pass
       # Här sker "eldväxlingen"

    def Block():
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def lvl_up(): 
        pass
       # Här ska lvl öka

    def get_attacked():
        pass
        # Här ska antalet liv minska

    def Drink_potion():
        pass

    def Eat_food():
        pass

class Monster():
    lvl = 0
    HP = 0
    STR = 0




#class Player():
    
#    def __init__(self, klass, lifes, capacity, armor):
#        self.lifes = lifes
#        self.scores = 0
#        self.armor = armor
#        self.did_hit = False
#        self.is_hitted = False
#        self.capacity = capacity
#        self.klass = klass

#    def print_info(self):
#        animate_typing(f"""
#                Character: {self.klass}
#                Health: {self.lifes}/{self.lifes} Armour: {self.armor}/{self.armor} 
#               Capacity: {self.capacity}/{self.capacity+5}""")
        
