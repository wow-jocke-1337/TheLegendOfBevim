class Player():
    def info(self, name, HP):
        self.name = name
        self.scores = 0
        self.HP = HP
        self.did_hit = False
        self.is_hitted = False

    def attack(self):
        pass
       # Här sker "eldväxlingen"

    def Block(self):
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def lvl_up(self): 
        pass
       # Här ska lvl öka

    def get_attacked(self):
        pass
        # Här ska antalet liv minska

    def Drink_potion(self):
        pass

    def Eat_food(self):
        pass

class Knight():
    def stats(HP, STR, ):
        pass