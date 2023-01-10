from Ascii_Art import*
from Text import*

class Player():
    name = ""
    lvl = 0
    HP = 0
    XP = 0 
    STR = 0

    def print_info():
        animate_typing(f""" 
        Name: {Player.name}
        LVL:  {Player.lvl}
        HP:   {Player.HP}
        XP:   {Player.XP}
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

    def gets_attacked():
        pass
        # Här ska antalet liv minska

    def Drink_potion():
        pass

    def Eat_food():
        pass

    def die():
        pass

class Monster():
    lvl = 0
    HP = 0
    STR = 0
