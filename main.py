import numpy as np
from graphics import art, move_x, move_o, grid_original, make_grid, how_to_grid_data





def show_grid(grid_data):
    temp_grid = make_grid(grid_data)
    print(temp_grid)


def intro():
    print(art)


def how_to_play():
    print("\n\n  Ola!")
    print("  These are the positions you could pick")
    show_grid(how_to_grid_data)


def mode_check(status):
    if status == 1:
        pass
    else:
        print("Human Vs. Computer update will come in the next patch. Pls wait till then.")


empty_grid_data = np.repeat("⬛", 9).reshape(3, 3)
grid = make_grid(empty_grid_data)



# show_grid(np.repeat("⬛", 9).reshape(3, 3))
2

# how_to_play()


def play_game():
    intro()
    mode = int(input("\nChoose a mode to play:\n  For Human Vs. Human, enter 1\n  For Human Vs. Computer, enter 2\n  :"))
    mode_check(mode)

play_game()