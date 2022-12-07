FILE_PATH = "./input.txt"

def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    print("Marker position: {}".format(find_marker(data)))


if __name__ == "__main__":
    main()