from Classes import*

class Weapon():
    def __init__(self,name,klass,str_mod,dex_mod,int_mod):
       self.name = name 
       self.klass = klass
       self.str_mod = str_mod
       self.dex_mod = dex_mod
       self.int_mod = int_mod

    def __repr__(self):
       return f"{self.name} ({self.klass})"
        
class Greatsword(Weapon):
   def __init__(self):
        super().__init__("Greatsword","Melee Weapon", 0.6, 0.2, 0.1)

class Axe(Weapon):
   def __init__(self):
       super().__init__("Axe","Melee Weapon", 0.5, 0.1, 0.1)
   
class Bow(Weapon):
   def __init__(self):
        super().__init__("Bow","Ranged Weapon", 0.2, 0.5, 0.1)

class Magical_staff(Weapon):
   def __init__(self):
        super().__init__("Magical Staff","Ranged Weapon", 0.1, 0.2, 0.5)

class Tommy_gun(Weapon):
   def __init__(self):
        super().__init__("Tommy Gun","Ranged Weapon", 0.1, 0.5, 0.3)

weapon_list = [Greatsword(),Tommy_gun(),Magical_staff(),Bow(),Axe()]


class Potion():
    def __init__(self,name,klass,effect) -> None:
        self.name = name
        self.klass = klass
        self.effect = effect
    
    def __repr__(self):
       return f"{self.name} ({self.klass})"

class Resource_Item():
    def __init__(self,name,klass,effect) -> None:
        self.name = name
        self.klass = klass
        self.effect = effect
    
    def __repr__(self):
       return f"{self.name} ({self.klass})"

class Healing_Item():
    def __init__(self,name,klass,healing_effect) -> None:
        self.name = name
        self.klass = klass
        self.healing_effect = healing_effect
    
    def __repr__(self):
       return f"{self.name} ({self.klass})"

class Healing_potion(Potion,Healing_Item):
    def __init__(self):
        super().__init__("Healing Potion","Potion",0.2)

class Mana_potion(Potion, Resource_Item):
    def __init__(self) -> None:
        super().__init__("Mana Potion","Potion",0.2)

potion_list = [Healing_potion(),Mana_potion()]

