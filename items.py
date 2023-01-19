from Classes import*

class Weapon():
    class IronSword():
        Dmg = 3 + Player.STR * 0.25 + Player.DEX * 0.5

    class Club():
        Dmg = 3 + Player.STR * 0.75 + Player.DEX * 0.1