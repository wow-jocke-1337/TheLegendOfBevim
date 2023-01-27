from Funktioner import*
from Rum import*
import os

def intiate_first_explore():
    time.sleep(2)
    animate_typing(prologue_start)
    time.sleep(2)
    os.system('cls')
    animate_typing(prologue_end_start)
    animate_typing(prologue_end)

# def initiate_explore():
#     time.sleep(2)
#     route_1 = random.choice()
#     route_2 = random.choice()
#     route_3 = random.choice()
#     animate_typing(f"""
#     Where do you want to go?
#     1 - {route_1}
#     2 - {route_2}
#     3 - {route_3}
    
#     Your Choice -->> """)
#     are_of_choice = input("")
#     if are_of_choice == 1:
#         animate_typing(route_1_prologue)
#     elif are_of_choice == 2:
#         animate_typing(route_2_prologue)
#     elif are_of_choice == 3:
#         animate_typing(route_3_prologue)
#     else:
#         animate_typing("""
#         You stopid! Choose an actual alternative, you not dreaming. Because if that were true I would be looking at the summary of your career. 
#         You should get a mirror, so you can see how dumb you are. 
        
#         /SOme wiSe ASian MAn
        
#         """)
#     time.sleep(2)
#     os.system('cls')