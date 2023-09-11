import numpy as np

grid_data = np.repeat(None, 9).reshape(3, 3)
keys = {
    "tl": (0, 0),
    "tm": (0, 1),
    "tr": (0, 2),
    "lm": (1, 0),
    "m": (1, 1),
    "rm": (1, 2),
    "ml": (2, 0),
    "bm": (2, 1),
    "br": (2, 2),
}
art = ""
grid = """
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |              
                |               |
_______________________________________________
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
_______________________________________________
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |

"""
X = """
        ?8888P
         `88'
    8b,_  88  _,d8
    88888SEAL88888
    8P~   88   ~?8
         ,88.
        d8888b
"""

Y = """
       ____
     ,' __ `.
    | ,'  `. |
    | | () | |
    \ `.__,' /
     `.____,`
"""

s = """
⭕❕⭕❕❌
➖➕➖➕➖
⭕❕❌❕⭕
➖➕➖➕➖
❌❕❌❕⭕ 
"""



def show_grid():
    print(grid)


def intro():
    print(art)

def how_to_play():
    show_grid()
    print("\n\nOla!")


def mode(status):
    if status == 1:
        pass
    else:
        print("Human Vs. Computer update will come in the next patch. Pls wait till then.")


# how_to_play()

print(s)