import random
import string
import time

import board
import game_controller
import player
from point import Point


def run_game(board_size):
    """PLAYER VS PLAYER SIMULATION BY COMPUTER"""
    player1_board = board.Board(board_size)
    player2_board = board.Board(board_size)
    player1_obj = player.Player(player1_board, "Player1")
    player2_obj = player.Player(player2_board, "Player2")

    player1_obj.board.auto_place_many_masted_ship(4)
    player1_obj.board.auto_place_many_masted_ship(3)
    player1_obj.board.auto_place_many_masted_ship(3)
    player1_obj.board.auto_place_many_masted_ship(2)
    player1_obj.board.auto_place_many_masted_ship(2)
    player1_obj.board.auto_place_many_masted_ship(2)
    player1_obj.board.auto_place_one_masted_ship()
    player1_obj.board.auto_place_one_masted_ship()
    player1_obj.board.auto_place_one_masted_ship()
    player1_obj.board.auto_place_one_masted_ship()

    player2_obj.board.auto_place_many_masted_ship(4)
    player2_obj.board.auto_place_many_masted_ship(3)
    player2_obj.board.auto_place_many_masted_ship(3)
    player2_obj.board.auto_place_many_masted_ship(2)
    player2_obj.board.auto_place_many_masted_ship(2)
    player2_obj.board.auto_place_many_masted_ship(2)
    player2_obj.board.auto_place_one_masted_ship()
    player2_obj.board.auto_place_one_masted_ship()
    player2_obj.board.auto_place_one_masted_ship()
    player2_obj.board.auto_place_one_masted_ship()

    player1_targets = [Point(x, y) for x in range(1, player1_board.size - 1) for y in
                       range(1, player1_board.size - 1)]
    player2_targets = [Point(x, y) for x in range(1, player2_board.size - 1) for y in
                       range(1, player2_board.size - 1)]

    round_number = 1
    while True:
        target_for_p1 = player1_targets[random.randint(0, len(player1_targets) - 1)]
        target_for_p2 = player2_targets[random.randint(0, len(player2_targets) - 1)]

        game_controller.clear()
        print("******************************  ROUND " + str(round_number) + "  ***************************")

        player1_obj.print_board_and_targets()
        player2_obj.print_board_and_targets()
        time.sleep(0.3)

        print(player1_obj.nickname + " move: " + string.ascii_uppercase[target_for_p1.y - 1] + str(target_for_p1.x))
        player1_obj.shoot(player2_board, target_for_p1.x, target_for_p1.y)
        player1_targets.remove(target_for_p1)
        if game_controller.is_game_finished(player1_obj, player2_obj):
            return
        time.sleep(0.3)

        print(player2_obj.nickname + " move: " + string.ascii_uppercase[target_for_p2.y - 1] + str(target_for_p2.x))
        player2_obj.shoot(player1_board, target_for_p2.x, target_for_p2.y)

        time.sleep(0.3)
        player2_targets.remove(target_for_p2)
        if game_controller.is_game_finished(player1_obj, player2_obj):
            return
        time.sleep(0.3)

        round_number = round_number + 1


run_game(10)
