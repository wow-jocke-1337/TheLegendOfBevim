from Classes import*

class Weapon():
    def __init__(self, name, klass, Dmg):
        self.name = name
        self.klass = klass
        self.Dmg = Dmg


class IronSword(Weapon):
    def __init__(self):
        super().__init__("Greatsword", "Melee Weapon",(f"Dmg:{3 + Player.STR * 0.5 + Player.DEX * 0.25}")) 
    pass


class Club(Weapon):
    def __init__(self):
        super().__init__("Club","Melee Weapon",(f"Dmg:{3 + Player.STR * 0.5 + Player.DEX * 0.25}"))
    pass


class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow","Ranged Weapon",(f"Dmg:{3 + Player.STR * 0.25 + Player.DEX * 0.5}"))
    pass


class Magical_Staff(Weapon):
    def __init__(self):
        super().__init__("Magical Staff","Ranged Weapon",(f"Dmg:{3 + Player.STR * 0.25 + Player.DEX * 0.5}") )
    pass

class Usable():
    def __init__(self, name):
        self.name = name
    pass

class Ammo():
    def __init__(self,arrows=10):
        self.arrows = arrows
    pass
