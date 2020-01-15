import string
from random import randint

import ship
from point import Point


class Board:
    """Class represent a board of ships"""

    def __init__(self, size):

        # creating bigger board, because coordinates starts with 1, and it will be easier to maintain
        self.size = size + 2

        self.board = [["0" for x in range(self.size)] for y in range(self.size)]

        self.ships = {
            "4 Masted Ship": [],
            "3 Masted Ship": [],
            "2 Masted Ship": [],
            "1 Masted Ship": []
        }

    def auto_place_many_masted_ship(self, n_of_masts):
        """ :returns a board with placed ships"""
        vertical = 1
        horizontal = 0
        draw = randint(0, 1)  # decide whether ship will be placed horizontal or vertical
        my_ship = ship.Ship()

        if draw == vertical:
            while True:
                found_suitable_position = True
                mast1 = Point(randint(1, len(self.board) - 2), randint(1, len(self.board) - (n_of_masts + 1)))
                for x in range(mast1.x - 1, mast1.x + 2):
                    for y in range(mast1.y - 1, mast1.y + (n_of_masts + 1)):
                        if self.board[x][y] != "0":  # checking if place around the ship is empty
                            found_suitable_position = False
                if found_suitable_position:
                    for x in range(mast1.x - 1, mast1.x + 2):
                        for y in range(mast1.y - 1, mast1.y + (n_of_masts + 1)):
                            if x == mast1.x and (mast1.y - 1 < y < mast1.y + n_of_masts):
                                self.board[x][y] = "-"
                                my_ship.masts.append(Point(x, y))
                    self.ships[str(n_of_masts) + " Masted Ship"].append(my_ship)
                    break

        if draw == horizontal:
            while True:
                found_suitable_position = True

                mast1 = Point(randint(1, len(self.board) - (n_of_masts + 1)), randint(1, len(self.board) - 2))

                for x in range(mast1.x - 1, mast1.x + (n_of_masts + 1)):
                    for y in range(mast1.y - 1, mast1.y + 2):
                        if self.board[x][y] != "0":
                            found_suitable_position = False
                if found_suitable_position:
                    for x in range(mast1.x - 1, mast1.x + (n_of_masts + 1)):
                        for y in range(mast1.y - 1, mast1.y + 2):
                            if y == mast1.y and (mast1.x - 1 < x < mast1.x + n_of_masts):
                                self.board[x][y] = "|"
                                my_ship.masts.append(Point(x, y))
                    self.ships[str(n_of_masts) + " Masted Ship"].append(my_ship)
                    break

        return self

    def auto_place_one_masted_ship(self):
        one_masted_ship = ship.Ship()
        while True:
            found_suitable_position = True
            mast1 = Point(randint(1, len(self.board) - 2), randint(1, len(self.board) - 2))
            for x in range(mast1.x - 1, mast1.x + 2):
                for y in range(mast1.y - 1, mast1.y + 2):
                    if self.board[x][y] != "0":
                        found_suitable_position = False
            if found_suitable_position:
                for x in range(mast1.x - 1, mast1.x + 2):
                    for y in range(mast1.y - 1, mast1.y + 2):
                        if x == mast1.x and (mast1.y - 1 < y < mast1.y + 1):
                            self.board[x][y] = "-"
                            one_masted_ship.masts.append(Point(x, y))
                self.ships["1 Masted Ship"].append(one_masted_ship)
                break

        return self

    def manual_place_many_masted_ship(self, point1, point2, n_of_masts):
        """ Place a ship with between given points"""

        if n_of_masts < 2:
            print("Number of masts must be grater than 1")
            return False

        if point1.x < 1 or point1.x > self.size - 2 or point1.y < 1 or point1.y > self.size - 2 or point2.x < 1 \
                or point2.x > self.size - 2 or point2.y < 1 or point2.y > self.size - 2:
            print("Coordinates out of board")
            return False
        if not (point1.x == point2.x or point1.y == point2.y):
            print("Points are not in horizontal or vertical line")
            return False
        if point1.x == point2.x:
            if abs(point1.y - point2.y) + 1 != n_of_masts:
                print("Wrong number of masts. Expected: " + str(n_of_masts))
                return False
            for i in range(point1.x - 1, point1.x + 2):
                if point1.y < point2.y:
                    for j in range(point1.y - 1, point2.y + 2):
                        if self.board[j][i] != "0":
                            print("No space here for the ship")
                            return False
                if point1.y > point2.y:
                    for j in range(point2.y - 1, point1.y + 2):
                        if self.board[j][i] != "0":
                            print("No space here for the ship")
                            return False
            my_ship = ship.Ship()
            if point1.y < point2.y:
                for i in range(point1.y, point2.y + 1):
                    self.board[i][point1.x] = "|"
                    mast = Point(i, point1.x)
                    my_ship.masts.append(mast)
            if point2.y < point1.y:
                for i in range(point2.y, point1.y + 1):
                    self.board[i][point1.x] = "|"
                    mast = Point(i, point1.x)
                    my_ship.masts.append(mast)
            self.ships[str(n_of_masts) + " Masted Ship"].append(my_ship)

        if point1.y == point2.y:
            if abs(point1.x - point2.x) + 1 != n_of_masts:
                print("Wrong number of masts. Expected: " + str(n_of_masts))
                return False
            for i in range(point1.y - 1, point1.y + 2):
                if point1.x < point2.x:
                    for j in range(point1.x - 1, point2.x + 2):
                        if self.board[i][j] != "0":
                            print("No space here for the ship")
                            return False
                if point1.x > point2.x:
                    for j in range(point2.x - 1, point1.x + 2):
                        if self.board[i][j] != "0":
                            print("No space here for the ship")
                            return False
            my_ship = ship.Ship()
            if point1.x < point2.x:
                for i in range(point1.x, point2.x + 1):
                    self.board[point1.y][i] = "-"
                    mast = Point(point1.y, i)
                    my_ship.masts.append(mast)
            if point2.x < point1.x:
                for i in range(point2.x, point1.x + 1):
                    self.board[point1.y][i] = "-"
                    mast = Point(point1.y, i)
                    my_ship.masts.append(mast)
            self.ships[str(n_of_masts) + " Masted Ship"].append(my_ship)
        return True

    def manual_place_one_masted_ship(self, point):

        for i in range(point.x - 1, point.x + 2):
            for j in range(point.y - 1, point.y + 2):
                if self.board[i][j] != "0":
                    print("Failed to place ship")
                    return False

        one_masted_ship = ship.Ship()
        self.board[point.y][point.x] = "-"
        one_masted_ship.masts.append(Point(point.y, point.x))
        self.ships["1 Masted Ship"].append(one_masted_ship)
        return True

    def print_decorated_board(b):
        print("  #  ", end="")
        for i in range(0, len(b.board) - 2):
            print(string.ascii_uppercase[i], end="  ")

        for i in range(1, len(b.board) - 1):
            print("", end="\n")
            for j in range(1, len(b.board) - 1):
                if j == 1:
                    print("{:3d}".format(i), end="  ")
                    print("{:3s}".format(b.board[i][j]), end="")
                else:
                    print("{:3s}".format(b.board[i][j]), end="")
        print()
