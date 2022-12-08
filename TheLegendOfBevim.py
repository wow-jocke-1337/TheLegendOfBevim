import random as rand

class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        pass
       # Här sker "eldväxlingen"

    def inc_scores(self): 
        pass
       # Här ska poängen öka

    def get_shot(self):
        pass
        # Här ska antalet liv minska


a_player = Player(3)       # Initiera en spelare med tre liv

while True:
    x = int(input("""Vad vill du göra bitch?
  (1)skjuta
  (2)bandagera --> +1 hp

    """))
    if x == 1:
        pass
    elif x == 2:
        pass

    a_player.get_shot()
    if a_player.lifes < 0:
        break

print("Haha du dog :)")

if Player == 1:
    print(f"Haha sämst")