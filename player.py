import string


class Player:
    def __init__(self, board, nickname):
        self.board = board
        self.nickname = nickname
        self.targets = [[" " for x in range(self.board.size)] for y in range(self.board.size)]

    def shoot(self, enemy_board, x, y):
        hit = False
        if enemy_board.board[x][y] == "|" or enemy_board.board[x][y] == "-":
            for key in enemy_board.ships:  # iterate over types of ships
                for i in range(len(enemy_board.ships[key])):  # iterate over specified type of ships
                    for j in range(len(enemy_board.ships[key][i].masts)):  # iterate over masts of the ship
                        if enemy_board.ships[key][i].masts[j].x == x and enemy_board.ships[key][i].masts[j].y == y:
                            # print(my_board.ships[key][i].masts)
                            enemy_board.ships[key][i].masts.pop(j)  # removing destroyed mast
                            if len(enemy_board.ships[key][i].masts) == 0:
                                print("You destroyed", key)
                                enemy_board.ships[key].pop(i)  # removing sunken ship
                                if len(enemy_board.ships[key]) == 0:
                                    enemy_board.ships.pop(key)  # removing key when all ships of same type sunken
                            else:
                                print("You hit", key)
                            enemy_board.board[x][y] = "X"
                            hit = True
                            self.targets[x][y] = "X"
                            return hit
        print("You missed")
        if self.targets[x][y] != "X":
            self.targets[x][y] = "0"
        return hit

    def print_board_and_targets(self):
        print(self.nickname.center(71, " "))

        print("  #  ", end="")
        for i in range(0, len(self.targets) - 2):
            print(string.ascii_uppercase[i], end="  ")
        print("  #  ", end="")
        for i in range(0, len(self.targets) - 2):
            print(string.ascii_uppercase[i], end="  ")

        for i in range(1, len(self.targets) - 1):
            print("", end="\n")
            for j in range(1, len(self.board.board) - 1):
                if j == 1:
                    print("{:3d}".format(i), end="  ")
                    print("{:3s}".format(self.board.board[i][j]), end="")
                else:
                    print("{:3s}".format(self.board.board[i][j]), end="")

            for j in range(1, len(self.targets) - 1):
                if j == 1:
                    print("{:3d}".format(i), end="  ")
                    print("{:3s}".format(self.targets[i][j]), end="")
                else:
                    print("{:3s}".format(self.targets[i][j]), end="")
        print()

    def print_targets(self):
        print("  #  ", end="")
        for i in range(0, len(self.targets) - 2):
            print(string.ascii_uppercase[i], end="  ")

        for i in range(1, len(self.targets) - 1):
            print("", end="\n")
            for j in range(1, len(self.targets) - 1):
                if j == 1:
                    print("{:3d}".format(i), end="  ")
                    print("{:3s}".format(self.targets[i][j]), end="")
                else:
                    print("{:3s}".format(self.targets[i][j]), end="")
        print()
