from Text import*
from Classes import*

low_mob_list = [wolf(),golem(),slime(),bats(),mountain_Lion()]
mid_mob_list = []
high_mob_list = [archdemon()]


attack_chance_list = [1,2,3,4,5,6]

    
class Monster:
    def __init__(self, name, HP, Def, STR, DEX, INT,spd):
        self.name = name
        self.HP = HP
        self.Def = Def
        self.STR = STR
        self.DEX = DEX
        self.INT = INT
        self.spd = spd
        
class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 10, 2, 3, 5, 1,1)

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 20, 4, 6, 3, 2,2)

class Dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 30, 8, 8, 2, 5,3)

class InitiateCombat:
    def __init__(self, player, monster_list):
        self.player = player
        self.monster_list = monster_list
        
    def start_combat(self):
        if not self.player.equipped_weapon:
            animate_typing("You do not have a weapon equipped.")
            animate_typing("Please select a weapon from your inventory to equip.")
            for i, item in enumerate(self.player.inventory):
                animate_typing(f"{i+1}. {item.name}")
            choice = int(input())
            self.player.equipped_weapon = self.player.inventory[choice-1]
            animate_typing(f"You have equipped {self.player.equipped_weapon.name}.")
            
        monster = random.choice(self.monster_list)
        animate_typing(f"A wild {monster.name} appeared!")
        animate_typing(f"{monster.name}'s HP: {monster.HP}")
        animate_typing(f"{monster.name}'s Defense: {monster.Def}")
        animate_typing(f"{monster.name}'s Strength: {monster.STR}")
        animate_typing(f"{monster.name}'s Dexterity: {monster.DEX}")
        animate_typing(f"{monster.name}'s Intelligence: {monster.INT}")
        animate_typing(f"{monster.name}'s Speed: {monster.spd}")
        
        while monster.HP > 0 and self.player.HP > 0:
            print("What would you like to do? (attack/block)")
            player_choice = input()
            if player_choice == "attack":
                hit_chance = (self.player.DEX + self.player.equipped_weapon.DEX + self.player.spd) - monster.spd
                if hit_chance > 0:
                    damage = self.player.equipped_weapon.damage + self.player.STR
                    monster.HP -= damage
                    print(f"You hit the {monster.name} for {damage} damage. {monster.name}'s remaining HP: {monster.HP}")
                else:
                    print(f"You missed the {monster.name}")
            elif player_choice == "block":
                block_chance = self.player.STR - monster.STR
                if block_chance > 0:
                    print(f"You successfully blocked the {monster.name}'s attack.")
                else:
                    damage = monster.STR - self.player.Def
                    self.player.HP -= damage
                    print(f"The {monster.name} hit you for {damage} damage. Your remaining HP: {self.player.HP}")
            else:
                print("Invalid choice. Please choose 'attack' or 'block'.")
            if monster.HP <= 0:
                print(f"You defeated the {monster.name}!")
                break
            if self.player.HP <= 0:
                print("You were defeated.")
                break

# def attack():
#         outcome = random.choice(list)
#         if outcome == 1 or 2 or 3 or 4:
#             animate_typing("\nYou hit the target!")
#             damage()
#         else:
#             animate_typing("\nYou missed.")

# def block():
#         outcome=random.choice(list)
#         if outcome==1 or outcome==2 or outcome==3:
#             animate_typing("\nSuccessfully blocked!")
#         else:
#             animate_typing("\nyou failed to block and took damage!"  + {Player.STR} *0.25)


# def Exit_Combat(): 
#         outcome= random.choice(list)
#         if outcome== 1 or 2:
#             animate_typing("\nSuccess! You ran away")
#         else:
#             animate_typing("\You Failed to Run Away!")




# def combat_choices():
#     combat_options = ("""
# What will you do now?

# 1 - Attack
# 2 - Block
# 3 - Check inventory
# 4 - Run Away

# Your choice --> """)
#     while True:
#         animate_typing(combat_options)
#         x=int(input("")) 
#         if x==1: 
#             attack()
#             break
#         elif x==2:
#             block()
#             break

# def damage():
#     while True:
#         outcome=random.choice(list)
#         if outcome== 1 or 2 or 3:
#             dmg =  Player.calculate_damage()
#             animate_typing(f"\nYou dealt {dmg} hitpoints.")
#             break
#         else:
#             animate_typing(f"\n\nYou dealt no damage.")
#             break
# #       if Barbarian:damage [0.45*Player.STR,0.10*Player.DEX]
# #       if Archer:damage[0.25*Player.STR,0.5*Player.DEX]
# #        if Mage:damage[0.4*Player.INT,0.2*Player.DEX]
# #        if Warrior:damage[0.3*Player.STR,0.3*Player.DEX]



          
# def Game_over():
#     if Player.HP > 50:
#         animate_typing("HP is at a stable level")
#         if 35 > Player.HP > 20:
#             animate_typing("You need to heal, HP is at a low level!")
#     if Player.HP <=0:
#         animate_typing("You got killed by the monster!")
#         exit()

  
# def initiate_combat():
#     combat_choices()
