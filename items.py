from Classes import*

class Weapon():
    def __init__(self, name, klass, dmg):
        self.name = name
        self.klass = klass
        self.dmg = dmg


class Greatsword():
    def __init__(self):
        self.name = "Greatsword" 
        self.klass = "Melee Weapon"
        self.dmg = (3+self.DEX*0.35 + self.INT * 0.2 + self.STR * 0.5) 
        pass

class Club(Weapon):
    def __init__(self, dmg):
        super().__init__("Club","Melee Weapon", dmg)
        pass


class Bow(Weapon):
    def __init__(self, dmg):
        super().__init__("Bow","Ranged Weapon",dmg)
        pass


class Magical_Staff(Weapon):
    def __init__(self,dmg):
        super().__init__("Magical Staff","Ranged Weapon",dmg)
        pass

class Consumable():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        pass

class Healing_potion(Consumable):
    def __init__(self,amount):
        super().__init__("Healing Potion", amount)
        pass

class Ammo():
    def __init__(self,arrows=10):
        self.arrows = arrows
        pass
