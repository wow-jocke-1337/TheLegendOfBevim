class Player():
    def info(self, name, HP):
        self.name = name
        self.lvl = 0
        self.did_hit = False
        self.is_hitted = False

    def print_info(self, Class):

        print(f""" 
        {self.name}
        LVL: {self.lvl} 
        HP: {Class.HP}

        
        """)

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


    def Knight():
        Class.STR = 20
        Class.HP = 100
        