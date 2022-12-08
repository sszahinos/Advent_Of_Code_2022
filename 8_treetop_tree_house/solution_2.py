FILE_PATH = "./input.txt"


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    trees = []
    for line in data:
        line = line.strip('\n')
        trees.append([int(c) for c in line])
    print("Highest scenic score: {}".format(get_scenic_score(trees)))


def get_scenic_score(trees):
    row_count = len(trees)
    col_count = len(trees[0])
    return analyze_scenic(trees, row_count, col_count)


def analyze_scenic(trees, row_count, col_count):
    high_score = 0
    row = 1
    while row < row_count - 1:
        col = 1
        while col < col_count - 1:
            score = check_visible(trees, row, col)
            if score > high_score:
                high_score = score
            col += 1
        row += 1
    return high_score


def check_visible(trees, row, col):
    return check_top_col(trees, row, col) \
           * check_left_row(trees, row, col) \
           * check_bot_col(trees, row, col) \
           * check_right_row(trees, row, col)


def check_top_col(trees, row, col):
    visible = 0
    origin_row = row
    while row > 0:
        visible += 1
        if trees[row - 1][col] >= trees[origin_row][col]:
            break
        row -= 1
    return visible


def check_bot_col(trees, row, col):
    visible = 0
    origin_row = row
    row_count = len(trees)
    while row < row_count - 1:
        visible += 1
        if trees[row + 1][col] >= trees[origin_row][col]:
            break
        row += 1
    return visible


def check_left_row(trees, row, col):
    visible = 0
    origin_col = col
    while col > 0:
        visible += 1
        if trees[row][col - 1] >= trees[row][origin_col]:
            break
        col -= 1
    return visible


def check_right_row(trees, row, col):
    visible = 0
    origin_col = col
    col_count = len(trees[0])
    while col < col_count - 1:
        visible += 1
        if trees[row][col + 1] >= trees[row][origin_col]:
            break
        col += 1
    return visible


if __name__ == "__main__":
    main()
