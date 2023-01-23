from Classes import*


#class Greatsword():
 #   def __init__(self):
 #       self.name = "Greatsword" 
#        self.klass = "Melee Weapon"
 #       self.str_mod = 0.5
#        self.dex_mod = 0.2
 #       self.int_mod = 0.1
#    
#    def __repr__(self):
#        return f"{self.name} ({self.klass})"


class Greatsword():
    def __init__(self,name,klass,str_mod,dex_mod,int_mod):
        self.name = name 
        self.klass = klass
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.int_mod = int_mod
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Club():
    def __init__(self):
        self.name = "Club" 
        self.klass = "Melee Weapon"
        self.str_mod = 0.4
        self.dex_mod = 0.3
        self.int_mod = 0.1
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Bow():
    def __init__(self):
        self.name = "Bow"
        self.klass = "Ranged Weapon"
        self.str_mod = 0.2
        self.dex_mod = 0.5
        self.int_mod = 0.1
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Magical_Staff():
    def __init__(self):
        self.name = "Magical Staff"
        self.klass = "Ranged Weapon"
        self.str_mod = 0.1
        self.dex_mod = 0.2
        self.int_mod = 0.4
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Healing_potion():
    def __init__(self):
        self.name = "Healing potion"
        self.klass = "Consumable"
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Mana_potion():
    def __init__(self) -> None:
        self.name = "Mana Potion"
        self.klass = "Consumable"
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"


class Arrows():
    def __init__(self):
        self.name = "Arrows"
        self.klass = "Consumable"
        self.arrows = 10


    def __repr__(self):
        return f"{self.name} ({self.klass})"