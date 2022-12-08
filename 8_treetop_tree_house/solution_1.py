FILE_PATH = "./input.txt"


def main():
    input_file = open(FILE_PATH, "r")
    data = input_file.readlines()
    trees = []
    for line in data:
        line = line.strip('\n')
        trees.append([int(c) for c in line])
    print("Number of visible trees: {}".format(get_visible_trees(trees)))


def get_visible_trees(trees):
    row_count = len(trees)
    col_count = len(trees[0])
    visible_trees = row_count * 2 + (col_count - 2) * 2
    visible_trees += count_inner_visible(trees, row_count, col_count)
    return visible_trees


def count_inner_visible(trees, row_count, col_count):
    visible_trees = 0
    row = 1
    while row < row_count - 1:
        col = 1
        while col < col_count - 1:
            if check_visible(trees, row, col):
                visible_trees += 1
            col += 1
        row += 1
    return visible_trees


def check_visible(trees, row, col):
    if check_top_col(trees, row, col) \
            or check_bot_col(trees, row, col) \
            or check_left_row(trees, row, col) \
            or check_right_row(trees, row, col):
        return 1
    return 0


def check_top_col(trees, row, col):
    origin_row = row
    taller_found = None
    while row > 0 and not taller_found:
        if trees[row - 1][col] >= trees[origin_row][col]:
            taller_found = 1
            break
        row -= 1
    return 0 if taller_found else 1


def check_bot_col(trees, row, col):
    origin_row = row
    row_count = len(trees)
    taller_found = None
    while row < row_count - 1 and not taller_found:
        if trees[row + 1][col] >= trees[origin_row][col]:
            taller_found = 1
            break
        row += 1
    return 0 if taller_found else 1


def check_left_row(trees, row, col):
    origin_col = col
    taller_found = None
    while col > 0 and not taller_found:
        if trees[row][col - 1] >= trees[row][origin_col]:
            taller_found = 1
            break
        col -= 1
    return 0 if taller_found else 1


def check_right_row(trees, row, col):
    origin_col = col
    col_count = len(trees[0])
    taller_found = None
    while col < col_count - 1 and not taller_found:
        if trees[row][col + 1] >= trees[row][origin_col]:
            taller_found = 1
            break
        col += 1
    return 0 if taller_found else 1


if __name__ == "__main__":
    main()
