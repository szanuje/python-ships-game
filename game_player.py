import game_controller
import time


# REAL GAME PLAYER VS PLAYER

def play():
    boards = game_controller.create_board()
    player1_obj = game_controller.create_player(boards[0])
    player2_obj = game_controller.create_player(boards[1])
    game_controller.place_ships(player1_obj)
    game_controller.place_ships(player2_obj)

    while True:
        clear()
        player1_obj.print_board_and_targets()
        game_controller.shoot(player1_obj, player2_obj)
        time.sleep(0.8)
        if game_controller.is_game_finished(player1_obj, player2_obj):
            return

        clear()
        player2_obj.print_board_and_targets()
        game_controller.shoot(player2_obj, player1_obj)
        time.sleep(0.8)
        if game_controller.is_game_finished(player1_obj, player2_obj):
            return


play()
