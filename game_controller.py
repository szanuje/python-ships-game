import string
import os
import board
import player
from point import Point

"""A set of functions needed to control the game and take input from user"""


def create_board():
    """ :returns two boards for players"""
    while True:
        try:
            board_size = int(input("Choose size of the board: "))
            if board_size < 5:
                raise ValueError
            break
        except ValueError:
            print("Wrong input")
    return [board.Board(board_size), board.Board(board_size)]


def create_player(player_board):
    """ :returns a player with board connected to him"""
    name = str(input("Chose player name: "))
    return player.Player(player_board, name)


def place_ships(my_player):
    """ place ships, automatically lub manually"""
    print(my_player.nickname + ", do you want to place your ships manually, or automatically?\nAuto-placing ships is "
                               "available when board is bigger than 9")
    print("(1) manual / (2) auto")
    while True:
        try:
            choice = int(input())
            if choice != 1 and choice != 2:
                raise ValueError
            break
        except ValueError:
            print("Wrong input")

    if choice == 2:
        my_player.board.auto_place_many_masted_ship(4)
        my_player.board.auto_place_many_masted_ship(3)
        my_player.board.auto_place_many_masted_ship(3)
        my_player.board.auto_place_many_masted_ship(2)
        my_player.board.auto_place_many_masted_ship(2)
        my_player.board.auto_place_many_masted_ship(2)
        my_player.board.auto_place_one_masted_ship()
        my_player.board.auto_place_one_masted_ship()
        my_player.board.auto_place_one_masted_ship()
        my_player.board.auto_place_one_masted_ship()
    if choice == 1:
        print("HOW TO PLACE SHIPS...")
        print(
            "Give 'x' and 'y' coordinates of two points, that represent corners of the ship.\nFor example, a 4 masted "
            "ship could have coordinates like: Point(2,3), Point(2,6")
        print(my_player.nickname + " place your ships...")
        for i in range(10):
            while True:
                success = False
                try:
                    if 0 <= i <= 5:
                        x_coords1 = int(input("Give 1st point's x coordinates to create 4 Masted ship (example 2)"))
                        y_coords1 = int(input("Give 1st point's y coordinates to create 4 Masted ship (example 3)"))
                        x_coords2 = int(input("Give 2st point's x coordinates to create 4 Masted ship (example 2 6)"))
                        y_coords2 = int(input("Give 2st point's y coordinates to create 4 Masted ship (example 2 6)"))
                        if i == 0:
                            success = my_player.board.manual_place_many_masted_ship(Point(x_coords1, y_coords1),
                                                                                    Point(x_coords2, y_coords2), 4)
                        if i == 1 or i == 2:
                            success = my_player.board.manual_place_many_masted_ship(Point(x_coords1, y_coords1),
                                                                                    Point(x_coords2, y_coords2), 3)
                        if i == 3 or i == 4 or i == 5:
                            success = my_player.board.manual_place_many_masted_ship(Point(x_coords1, y_coords1),
                                                                                    Point(x_coords2, y_coords2), 2)
                    if 6 <= i <= 9:
                        x_coords1 = int(input("Give point's x coordinates to create 1 Masted ship (example 2)"))
                        y_coords1 = int(input("Give point's y coordinates to create 1 Masted ship (example 3)"))
                        success = my_player.board.manual_place_one_masted_ship(Point(x_coords1, y_coords1))
                    if success:
                        my_player.board.print_decorated_board()
                        break
                except ValueError:
                    print("Wrong input")


def shoot(me, enemy):
    print(me.nickname + ", shoot!")
    while True:
        try:
            coords = str(input("Give coordinates to shoot (ex.: C2): "))
            x_coords = int(coords[1:])
            y_coords = string.ascii_uppercase.index(coords[0]) + 1
            if x_coords > enemy.board.size - 2 or x_coords < 1 or y_coords > enemy.board.size - 2 or y_coords < 1:
                raise ValueError
            # print(x_coords)
            # print(y_coords)
            me.shoot(enemy.board, x_coords, y_coords)
            break
        except ValueError:
            print("Wrong input")


def is_game_finished(player1, player2):
    if len(player1.board.ships) == 0:
        print()
        print("**************")
        print(player2.nickname.center(14, "*"))
        print("*  YOU WON!  *")
        print("**************")
        print()
        return True
    if len(player2.board.ships) == 0:
        print()
        print("**************")
        print(player1.nickname.center(14, "*"))
        print("*  YOU WON!  *")
        print("**************")
        print()
        return True
    return False


def clear():
    """ clear console"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
