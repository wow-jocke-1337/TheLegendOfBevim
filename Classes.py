class Player():
    name = ""
    lvl = 0
    STR = 0
    HP = 0
    did_hit = False
    is_hitted = False

    def print_info():

        print(f""" 
        {Player.name}
        LVL: {Player.lvl} 
        HP: {Player.HP}

        
        """)

    def attack():
        pass
       # Här sker "eldväxlingen"

    def Block():
        pass
       # Spelaren väljer att blocka nästa tur och försöka få monstret att bli stunned

    def lvl_up(): 
        pass
       # Här ska lvl öka

    def get_attacked():
        pass
        # Här ska antalet liv minska

    def Drink_potion():
        pass

    def Eat_food():
        pass

    

        