FILE_PATH = "./input.txt"


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    print("Marker position: {}".format(find_marker(data)))


def find_marker(signal):
    signal_len = len(signal[0])
    i = 0
    while i < signal_len - 4:
        if check_packet(signal[0], i):
            return i + 4
        i += 1


def check_packet(signal, start):
    i = 0
    while i < 3:
        j = 1
        while j <= 3 - i:
            if signal[start + i] == signal[start + j + i]:
                return 0
            j += 1
        i += 1
    return 1


if __name__ == "__main__":
    main()
