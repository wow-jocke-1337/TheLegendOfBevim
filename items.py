from Classes import*

class Weapon():
    def __init__(self, name, klass, Dmg):
        self.name = name
        self.klass = klass
        self.Dmg = Dmg


class IronSword(Weapon):
    def __init__(self, Dmg):
        super().__init__("Greatsword", "Melee Weapon",Dmg) 
        pass

class Club(Weapon):
    def __init__(self, Dmg):
        super().__init__("Club","Melee Weapon", Dmg)
        pass


class Bow(Weapon):
    def __init__(self, Dmg):
        super().__init__("Bow","Ranged Weapon",Dmg)
        pass


class Magical_Staff(Weapon):
    def __init__(self,Dmg):
        super().__init__("Magical Staff","Ranged Weapon",Dmg)
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
