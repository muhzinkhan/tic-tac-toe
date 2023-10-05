import numpy as np
import player
from os import system, name
from graphics import art, make_grid, how_to_grid_data


is_game_on = True


def clear():
    """Clears the screen according to the os."""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def show_grid(grid_data):
    temp_grid = make_grid(grid_data)
    print(temp_grid)


def intro():
    print(art)


def how_to_play():
    print("\n\n  Ola!")
    print("  These are the positions you could pick")
    show_grid(how_to_grid_data)
    input("Press Enter to continue...")


def run_mode(status):
    if status == 1:
        multiplayer()
    else:
        input("Human Vs. Computer update will come in the next patch. Pls wait till then.\n\nPress enter to continue...")
        clear()
        run()


def multiplayer():
    main_grid_data = np.repeat("⬛", 9).reshape(3, 3)
    player1 = player.Player()
    player2 = player.Player()
    show_grid(main_grid_data)

    while True:
        main_grid_data = player1.play_move(main_grid_data)
        player.Player.play_count += 1
        clear()
        show_grid(main_grid_data)

        if is_game_over(player1):
            break

        main_grid_data = player2.play_move(main_grid_data)
        player.Player.play_count += 1
        clear()
        show_grid(main_grid_data)

        if is_game_over(player2):
            break

    print(f"\nScore:  Player1: {player1.score}")
    print(f"        Player2: {player2.score}")
    if input("\n play again? (y/n)") == "y":
        del player1
        del player2
        player.Player.play_count = 0
        player.pos_cord = {
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
        player.id_gen = player.identity()
        player.symbol_gen = player.symbol_()
        clear()
        run()


def is_game_over(user):

    for i in range(3):
        if user.player_table[i][0] == user.player_table[i][1] == user.player_table[i][2] == 1:
            user.score += 1
            print(f"Player {user.id} wins!😊🏆")
            return True
        elif user.player_table[0][i] == user.player_table[1][i] == user.player_table[2][i] == 1:
            user.score += 1
            print(f"Player {user.id} wins!😊🏆")
            return True
    if user.player_table[0][0] == user.player_table[1][1] == user.player_table[2][2] == 1:
        user.score += 1
        print(f"Player {user.id} wins!😊🏆")
        return True
    elif user.player_table[0][2] == user.player_table[1][1] == user.player_table[2][0] == 1:
        user.score += 1
        print(f"Player {user.id} wins!😊🏆")
        return True
    elif user.play_count == 9:
        print(f"It's a Tie!")
        return True

    return False


def run():
    intro()
    how_to_play()
    mode = int(
        input("\nChoose a mode to play:\n  For Human Vs. Human, enter 1\n  For Human Vs. Computer, enter 2\n  :"))
    clear()
    run_mode(mode)


run()
