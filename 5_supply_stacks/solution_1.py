import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    input_file = open(sys.argv[1], "r")
    data = input_file.readlines()
    stacks = get_stacks(data)
    moves = get_moves(data)
    top_crates = get_top_crates(stacks, moves)

    print("Top crates are: ", end='')
    for crate in top_crates:
        print("{}".format(crate), end='')
    print()

def get_stacks(data):
    stacks_num = int(len(data[0]) / 4)
    size = 0
    
    for row in data:
        if row[1] == '1':
            break
        size += 1
    stacks = []
    size -= 1
    aux = stacks_num
    while aux > 0:
        stacks.append([])
        aux -= 1
    while size >= 0:
        data_pos = 1
        for stack in range(stacks_num):
            if data[size][data_pos] != ' ':
                stacks[stack].append(data[size][data_pos])
            data_pos += 4
        size -= 1
    return stacks

def get_moves(data):
    i = 0
    while data[i][0] != 'm':
        i += 1
    num_moves = len(data) - i
    moves = []
    count = 0
    while i < len(data):
        moves.append([])
        aux = data[i].split(sep=' ')
        moves[count] = [int(aux[1]), int(aux[3]) - 1, int(aux[5]) - 1]
        i += 1
        count += 1
    return moves

def get_top_crates(stacks, moves):
    for move in moves:
        steps = 0
        while steps < move[0]:
            crate = stacks[move[1]].pop(-1)
            stacks[move[2]].append(crate)
            steps += 1
    top_crates = []
    for col in stacks:
        top_crates.append(col.pop())
    return top_crates

if __name__ == "__main__":
    main()
