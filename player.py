import numpy as np
from graphics import moves


def identity():
    for i in range(1, 3):
        yield i


def symbol_():
    for i in moves:
        yield i


id_gen = identity()
symbol_gen = symbol_()
pos_cord = {
    '1': (0, 0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
    '9': (2, 2)
}


class Player:
    play_count = 0

    def __init__(self):
        self.id = id_gen.__next__()
        self.symbol = symbol_gen.__next__()
        self.score = 0
        self.player_table = np.repeat(0, 9).reshape(3, 3)

    def play_move(self, grid_data):
        cords = False
        pos = 0
        pos = input(f"Player {self.id}, pick a position to place your move: ")
        while not cords:
            try:
                cords = pos_cord[pos]
            except KeyError:
                pos = input(f"Please enter a valid non-occupied-position: ")

        # update self.player_grid
        self.player_table[cords[0]][cords[1]] = 1

        # Update the main grid
        grid_data[cords[0]][cords[1]] = self.symbol

        # delete the current position from pos_cord
        del pos_cord[pos]

        return grid_data

