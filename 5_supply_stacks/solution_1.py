import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    input_file = open(sys.argv[1], "r")
    data = input_file.readlines()
    stacks = get_stacks(data)
    moves = get_moves(data)

def get_stacks(data):
    stacks_num = int(len(data[0]) / 4)
    size = 0
    
    for row in data:
        if row[1] == '1':
            break
        size += 1
    stacks = []
    size -= 1
    aux = size
    while aux >= 0:
        stacks.append([])
        aux -= 1
    while size >= 0:
        data_pos = 1
        for stack in range(stacks_num):
            if (data[size][data_pos] != ' '):
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
        moves[count] = [int(data[i][5]), int(data[i][12]), int(data[i][17])]
        i += 1
        count += 1
    print(moves)
        

if __name__ == "__main__":
    main()
