from Classes import*

class Weapon():
    def __init__(self, name, klass, str_mod, dex_mod, int_mod, abilities:list):
        self.name = name 
        self.klass = klass
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.int_mod = int_mod
        self.abilities = abilities
    
    def __repr__(self):
        return f"{self.name} ({self.klass})"
        
        
class Greatsword(Weapon):
    def __init__(self):
        super().__init__("Greatsword","Melee Weapon", 0.6, 0.2, 0.1,["Cleave","Heavy Strike"])


class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe","Melee Weapon", 0.5, 0.1, 0.1,["Whirwind","Critical Strike"])

class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow","Ranged Weapon", 0.2, 0.5, 0.1,["Piercing Shot","Multi-Shot"])


class Magical_staff(Weapon):
    def __init__(self):
        super().__init__("Magical Staff","Ranged Weapon", 0.1, 0.2, 0.5,["Fireball","Frost Nova"])


class Tommy_gun(Weapon):
    def __init__(self):
        super().__init__("Tommy Gun","Ranged Weapon", 0.1, 0.5, 0.3,["Suppressive Fire","Rapid Fire"])


class Moonlight_greatsword(Weapon):
    def __init__(self):
        super().__init__("Moonlight Greatsword","Melee Weapon", 0.2, 0.2, 0.4,["Moonlight Blade","Magic Shield"])


class Shovel(Weapon):
    def __init__(self):
        super().__init__("Shovel","Melee Weapon", 0.5, 0.3, 0.1,["Dig","Smash"])

class Hand_of_god(Weapon):
    def __init__(self):
        super().__init__("Hand of God","Divine Weapon", 10, 30, 10,["Smite","Adamas"])


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

weapon_list = [Greatsword(),Tommy_gun(),Magical_staff(),Bow(),Axe(),Shovel(),Moonlight_greatsword()]
