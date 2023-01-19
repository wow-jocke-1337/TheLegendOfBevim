from Classes import*

class Weapon():
    class IronSword():
        Dmg = 3 + Player.STR * 0.25 + Player.DEX * 0.5

    class Club():
        Dmg = 3 + Player.STR * 0.75 + Player.DEX * 0.1

    class Bow():
        Dmg = 3 + Player.STR * 0.15 + Player.DEX * 0.70 

    class Magical_Staff():
        Dmg = 3 + Player.STR * 0.10 + Player.DEX * 0.30 + Player.INT *0.6
