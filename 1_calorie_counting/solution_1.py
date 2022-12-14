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
    max_cal = 0
    for elve_cal in elves:
        if elve_cal > max_cal:
            max_cal = elve_cal
    return max_cal

if __name__ == "__main__":
    main()