from Classes import*

class Weapon():
    def __init__(self, name, str_mod, dex_mod, int_mod, klass):
        self.name = name
        self.klass = klass
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.int_mod = int_mod

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


class Consumable():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        pass

class Healing_potion():
    def __init__(self):
        self.name = "Healing potion"
        self.amount = 1
        
class Mana_potion():
    def __init__(self) -> None:
        self.name = "Mana Potion"
        self.amount = 1

class Arrows():
    def __init__(self,arrows=10):
        self.name = "Arrows"
        self.arrows = arrows
        
