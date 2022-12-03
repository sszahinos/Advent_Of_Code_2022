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
    i = 1
    group = []
    for rucksack in rucksacks:
        group.append(rucksack.strip('\n'))
        if i % 3 == 0:
            total_priorities += find_priority(group)
            group.clear()
        i += 1
    return total_priorities


def find_priority(group):
    for item in group[0]:
        if find_item(group, item):
            return ord(item) - 38 if item.isupper() else ord(item) - 96
    return -1


def find_item(group, item):
    for same_item in group[1]:
        if item == same_item:
            for same_item2 in group[2]:
                if item == same_item2:
                    return 1
    return 0


if __name__ == "__main__":
    main()
