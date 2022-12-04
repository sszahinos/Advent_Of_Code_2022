import sys


def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    input_file = open(sys.argv[1], "r")
    data = input_file.readlines()
    areas = []
    for group_area in data:
        groups = group_area.strip('\n').split(sep=',')
        for group in groups:
            areas.append(group.split(sep="-"))
    areas = [[int(num) for num in sub] for sub in areas]
    print("Redundant groups: {}".format(check_groups(areas)))


def check_groups(areas):
    count = 0
    i = 1
    group = []

    for area in areas:
        group.append(area)
        if i % 2 == 0:
            if is_redundant(group[0], group[1]):
                count += 1
            group.clear()
        i += 1
    return count


def is_redundant(area1, area2):
    start = area1[0]
    end = area1[1]

    while start <= end:
        if find_miniarea(start, area2) == 1:
            return 1
        start += 1
    return 0


def find_miniarea(miniarea, area):
    start = area[0]
    while start <= area[1]:
        if start == miniarea:
            return 1
        start += 1
    return 0


if __name__ == "__main__":
    main()
