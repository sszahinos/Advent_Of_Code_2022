import sys


def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    input_file = open(sys.argv[1], "r")
    data = input_file.readlines()
    print("The sum of the priorities is: {}".format(get_priorities(data)))


def get_priorities(rucksacks):
    total_priorities = 0
    for rucksack in rucksacks:
        total_priorities += find_priority(rucksack.strip('\n'))
    return total_priorities


def find_priority(rucksack):
    mid = int(len(rucksack) / 2)
    i = 0
    while i < mid:
        if find_item(rucksack, i, mid):
            if rucksack[i].isupper():
                return ord(rucksack[i]) - 38
            else:
                return ord(rucksack[i]) - 96
        i += 1
    return -1


def find_item(rucksack, wrong_item, mid):
    rucksack_len = int(len(rucksack))
    while mid < rucksack_len:
        if rucksack[mid] == rucksack[wrong_item]:
            return 1
        mid += 1
    return 0


if __name__ == "__main__":
    main()
