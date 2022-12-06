FILE_PATH = "./input.txt"
MARK_LEN = 14

def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    print("Marker position: {}".format(find_marker(data)))


def find_marker(signal):
    signal_len = len(signal[0])
    i = 0
    while i < signal_len - MARK_LEN:
        if check_packet(signal[0], i):
            return i + MARK_LEN
        i += 1


def check_packet(signal, start):
    i = 0
    while i < MARK_LEN - 1:
        j = 1
        while j <= MARK_LEN - 1 - i:
            if signal[start + i] == signal[start + j + i]:
                return 0
            j += 1
        i += 1
    return 1


if __name__ == "__main__":
    main()
