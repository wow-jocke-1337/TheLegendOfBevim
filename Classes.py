from Ascii_Art import*
from Text import*

class Player():
    name = ""
    lvl = 0
    HP = 0
    XP = 0 
    STR = 0
    inventory = []
    inventory_slots = 3
    klass = ""

    def print_info():
        animate_typing_fast(f""" 
        {Player.name} the {Player.klass}
        LVL:  {Player.lvl}
        XP:   {Player.XP}
        HP:   {Player.HP}
        Strength: {Player.STR}
        Inventory slots: {Player.inventory_slots}

        """)

    def print_inventory():
        time.sleep(1)
        print()
        animate_typing(f"\n{Player.inventory}")

    def attack():
        pass
       # Här sker "eldväxlingen"

    def Block():
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def add_item():
        pass
        # här läggs nånting in i spelarens inventory
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


class Wolf():
    lvl = 0
    HP = 10
    STR = 2

class Golem():
    lvl = 0
    HP = 30
    STR = 0.5

class slime():
    lvl = 0
    HP = 7
    STR = 3

class mountain_Lion():
    lvl=0
    HP=45
    STR=5

class Bats():
    lvl=0
    HP=2
    STR=1

class archdemon():
    lvl=0
    HP=70
    STR=10.5

class Bevins_bror():
    lvl=0
    HP=100
    STR=8