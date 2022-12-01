import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    inputFile = open(sys.argv[1], "r")
    data = inputFile.readlines()
    analyze_elves(data)

def analyze_elves(data):
    elve = 0
    elves = []
    elves.append(0)
    for calories in data:
        if calories == '\n':
            elve += 1
            elves.append(0)
        else:
            elves[elve] += int(calories)
    print("Max calories: {}".format(get_max_cal(elves)))

def get_max_cal(elves):
    max_cals = [0, 0, 0]
    for elve_cal in elves:
        for cal in max_cals:
            if elve_cal > cal:
                update_max(elve_cal, max_cals)
                break
    total = 0
    for cal in max_cals:
        total += cal
    return total

def update_max(new_cal, cals):
    for index, cal in enumerate(cals):
        if new_cal > cal:
            aux = cal
            cals[index] = new_cal
            new_cal = aux



if __name__ == "__main__":
    main()