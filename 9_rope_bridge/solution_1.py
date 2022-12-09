FILE_PATH = "./test.txt"


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    movements = []
    for line in data:
        movements.append(line.strip('\n').split(" "))
    for movement in movements:
        movement[1] = int(movement[1])
    print(movements)
    print("Number of cells visited: {}".format(get_visited_cells(movements)))


def get_visited_cells(movements):
    visited_cells = 0
    ht_movement = [[0, 0], [0, 0], {}]
    for movement in movements:
        if movement[0] == 'U':
            move_up(movement[1], ht_movement)
        elif movement[0] == 'L':
            move_left(movement[1], ht_movement)
        elif movement[0] == 'D':
            move_down(movement[1], ht_movement)
        else:  # L
            move_right(movement[1], ht_movement)
    return visited_cells

# def get_configuration(movements):
#     start_position = [0, 0]
#     max_length = [0, 0, 0, 0]
#     for movement in movements:
#         if movement[0] == 'U':
#             max_length[0] += movement[1]
#         elif movement[0] == 'L':
#             max_length[1] += movement[1]
#         elif movement[0] == 'D':
#             max_length[2] += movement[1]
#         else:  # L
#             max_length[3] += movement[1]
#     start_position = [max_length[0], max_length[1]]


def move_up(move, ht_movement):
    aux = ht_movement[0]
    ht_movement[0][1] += 1
    move_tail(ht_movement, aux)

def move_left(move, ht_movement):
    aux = ht_movement[0]
    ht_movement[0][0] -= 1
    move_tail(ht_movement, aux)

def move_down(move, ht_movement):
    aux = ht_movement[0]
    ht_movement[0][1] -= 1
    move_tail(ht_movement, aux)

def move_right(move, ht_movement):
    aux = ht_movement[0]
    ht_movement[0][0] += 1
    move_tail(ht_movement, aux)

def move_tail(ht_movement, aux):
    if not tail_is_touching(ht_movement):
        ht_movement[1] = aux
        ht_movement[2].append(aux)

def tail_is_touching(ht_movement):
    if ht_movement[0][0] == ht_movement[1][0]: # same row
        if ht_movement[0][1]

if __name__ == "__main__":
    main()
