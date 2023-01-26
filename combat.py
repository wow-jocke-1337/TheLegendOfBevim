# from Text import*
# from Classes import*

# low_mob_list = [wolf(),golem(),slime(),bats(),mountain_Lion(),Orc()]
# mid_mob_list = [dragon(),lower_class_demon(),upper_class_demon(), kikimora()]
# high_mob_list = [archdemon()]


# attack_chance_list = [1,2,3,4,5,6]


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
#     while True:
#         animate_typing(combat_options)
#         x=int(input("")) 
#         if x==1: 
#             attack()
#             break
#         elif x==2:
#             block()
#             break
#         elif x==3:
#             player.print_inventory()
#             break
#         elif x==4:
#             animate_typing(f"\nYou Died")
#             exit()
#         else:
#             animate_typing(f"\nChoose one of the alternatives.")
#             break
# ("""

# 1 - Attack
# 2 - Block
# 3 - Check_inventory
# 4 - Run_Away

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
#             animate_typing("\nYou dealt hitpoints.")
#             Player.calculate_damage()
#         else:
#             animate_typing("\n\nYou dealt no damage.")
#         if Barbarian:damage [0.45*Player.STR,0.10*Player.DEX]
#         if Archer:damage[0.25*Player.STR,0.5*Player.DEX]
#         if Mage:damage[0.4*Player.INT,0.2*Player.DEX]
#         if Warrior:damage[0.3*Player.STR,0.3*Player.DEX]



          
# def Game_over():
#     if Player.HP >50:
#         animate_typing("HP is at a stable level")
#         if Player.HP >20:
#             animate_typing("You need to heal HP is at a low level!")
#     if Player.HP <=0:
#         animate_typing("You got killed by the monster!")
#         exit()





    

        
# def initiate_combat():
#     choices()
