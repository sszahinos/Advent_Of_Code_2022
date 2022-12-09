FILE_PATH = "./input.txt"


class Rope:
    def __init__(self, row=0, col=0, name=None):
        self.position = Coord()
        self.name = name
        self.position.row = row
        self.position.col = col


class Coord:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def __key(self):
        return self.row, self.col

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.__key() == other.__key()

    def __str__(self):
        return "r{} / c{}".format(self.row, self.col)

    def __hash__(self):
        return hash(self.__key())


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    movements = []
    for line in data:
        movements.append(line.strip('\n').split(" "))
    for movement in movements:
        movement[1] = int(movement[1])
    print("Number of cells visited: {}".format(get_visited_cells(movements)))
    #test_tail_is_touching()


def get_visited_cells(movements):
    head = Rope(name="head")
    tail = Rope(name="tail")
    ht_movement = [head, tail, set()]
    ht_movement[2].add(Coord())
    #print("Head in {} | Tail in {}".format(ht_movement[0].position, ht_movement[1].position))
    for movement in movements:
        #print("START COMMAND")
        if movement[0] == 'U':
            move_up(movement[1], ht_movement)
        elif movement[0] == 'L':
            move_left(movement[1], ht_movement)
        elif movement[0] == 'D':
            move_down(movement[1], ht_movement)
        else:  # L
            move_right(movement[1], ht_movement)
    #for item in ht_movement[2]:
    #    print(item)
    # print("test tail_is_touching")
    return len(ht_movement[2])


def move_up(move, ht_movement):
    i = 1
    while i <= move:
        aux = Coord(ht_movement[0].position.row, ht_movement[0].position.col)
        # print("U aux ", aux)
        ht_movement[0].position.row += 1  ## Realmente se mueve move veces, toca bucle
        # print("Upost aux ", aux)
        move_tail(ht_movement, aux)
        # print("Head in {} | Tail in {}".format(ht_movement[0].position, ht_movement[1].position))
        i += 1


def move_left(move, ht_movement):
    i = 1
    while i <= move:
        aux = Coord(ht_movement[0].position.row, ht_movement[0].position.col)
        # print("L aux ", aux)
        ht_movement[0].position.col -= 1
        move_tail(ht_movement, aux)
        # print("Head in {} | Tail in {}".format(ht_movement[0].position, ht_movement[1].position))
        i += 1


def move_down(move, ht_movement):
    i = 1
    while i <= move:
        aux = Coord(ht_movement[0].position.row, ht_movement[0].position.col)
        # print("D aux ", aux)
        ht_movement[0].position.row -= 1
        move_tail(ht_movement, aux)
        # print("Head in {} | Tail in {}".format(ht_movement[0].position, ht_movement[1].position))
        i += 1


def move_right(move, ht_movement):
    i = 1
    while i <= move:
        aux = Coord(ht_movement[0].position.row, ht_movement[0].position.col)
        # print("R aux ", aux)
        ht_movement[0].position.col += 1
        move_tail(ht_movement, aux)
        # print("Head in {} | Tail in {}".format(ht_movement[0].position, ht_movement[1].position))
        i += 1


def move_tail(ht_movement, aux):
    #print("Before move H>{} T>{}: ".format(ht_movement[0].position, ht_movement[1].position))
    if not tail_is_touching(ht_movement):
        #print("- Se mueve a ", aux)
        ht_movement[2].add(Coord(aux.row, aux.col))
        ht_movement[1].position = aux


def tail_is_touching(ht_movement):
    #print("H>{} T>{}".format(ht_movement[0].position, ht_movement[1].position))
    return (abs(ht_movement[0].position.row - ht_movement[1].position.row) <= 1
            and abs(ht_movement[0].position.col - ht_movement[1].position.col) <= 1) \
            or (ht_movement[0].position.row == ht_movement[1].position.row
               and ht_movement[0].position.col == ht_movement[1].position.col)


def test_tail_is_touching():
    print("-- TEST --")
    print("01 yes ", tail_is_touching([Rope(row=1, col=-1), Rope()]))
    print("02 yes ", tail_is_touching([Rope(row=1, col=0), Rope()]))
    print("03 yes ", tail_is_touching([Rope(row=1, col=1), Rope()]))
    print("04 yes ", tail_is_touching([Rope(row=-1, col=-1), Rope()]))
    print("05 yes ", tail_is_touching([Rope(row=-1, col=0), Rope()]))
    print("06 yes ", tail_is_touching([Rope(row=-1, col=1), Rope()]))
    print("07 yes ", tail_is_touching([Rope(row=0, col=-1), Rope()]))
    print("08 yes ", tail_is_touching([Rope(row=0, col=-1), Rope()]))
    print("09 no ", tail_is_touching([Rope(row=2), Rope()]))
    print("10 no ", tail_is_touching([Rope(row=-2), Rope()]))
    print("11 no ", tail_is_touching([Rope(col=2), Rope()]))
    print("12 no ", tail_is_touching([Rope(col=-2), Rope()]))
    print("13 yes ", tail_is_touching([Rope(row=4, col=3), Rope(row=3, col=4)]))
    print("14 no ", tail_is_touching([Rope(row=4, col=2), Rope(row=3, col=4)]))
    print("15 no ", tail_is_touching([Rope(row=4, col=0), Rope(row=3, col=4)]))


if __name__ == "__main__":
    main()
