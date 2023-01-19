from Classes import*


class IronSword():
    Dmg = 3 + Player.STR * 0.25

class Bow():
    Dmg= 3 + Player.STR * 0.15 + Player.DEX * 0.70 + Player.INT * 0.1

class Magical_Staff():
    Dmg= 3 + Player.STR * 0.10 + Player.DEX * 0.30 + Player.INT *0.6