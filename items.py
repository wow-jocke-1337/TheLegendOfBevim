from Classes import*

class Item():
    def __init__(self, name, klass) -> None:
        self.name = name
        self.klass = klass
        

class Greatsword():
    def __init__(self):
        self.name = "Greatsword" 
        self.klass = "Melee Weapon"
        self.str_mod = 0.5
        self.dex_mod = 0.2
        self.int_mod = 0.1

class Club():
    def __init__(self):
        self.name = "Club" 
        self.klass = "Melee Weapon"
        self.str_mod = 0.4
        self.dex_mod = 0.3
        self.int_mod = 0.1

class Bow():
    def __init__(self):
        self.name = "Bow"
        self.klass = "Ranged Weapon"
        self.str_mod = 0.2
        self.dex_mod = 0.5
        self.int_mod = 0.1


class Magical_Staff():
    def __init__(self):
        self.name = "Magical Staff"
        self.klass = "Ranged Weapon"
        self.str_mod = 0.1
        self.dex_mod = 0.2
        self.int_mod = 0.4

class Healing_potion():
    def __init__(self):
        self.name = "Healing potion"
        self.klass = "Consumable"
        
class Mana_potion():
    def __init__(self) -> None:
        self.name = "Mana Potion"
        self.klass = "Consumable"

class Arrows():
    def __init__(self):
        self.name = "Arrows"
        self.klass = "Consumable"
        self.arrows = 10

        
