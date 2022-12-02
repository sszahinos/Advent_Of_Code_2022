import sys


def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        sys.exit()
    input_file = open(sys.argv[1], "r")
    data = input_file.readlines()
    # split into a [x, y] array
    game_rounds = []
    for index, game_round in enumerate(data):
        game_rounds.append(game_round.strip('\n').split())
    print("Max score possible: {}".format(check_game(game_rounds)))


# This version optimizes the selections but is not required
# def check_game(game_rounds):
#     scores = [
#         calc_score(select_game('A', 'B', 'C', game_rounds)),
#         calc_score(select_game('A', 'C', 'B', game_rounds)),
#         calc_score(select_game('B', 'A', 'C', game_rounds)),
#         calc_score(select_game('B', 'C', 'A', game_rounds)),
#         calc_score(select_game('C', 'A', 'B', game_rounds)),
#         calc_score(select_game('C', 'B', 'A', game_rounds))
#     ]
#     return max(scores)
def check_game(game_rounds):
   return (calc_score(select_game(game_rounds)))


# This version optimizes the selections but is not required
# def select_game(x, y, z, game_rounds):
#     for game_round in game_rounds:
#         if game_round[1] == 'X':
#             game_round[1] = x
#         elif game_round[1] == 'Y':
#             game_round[1] = y
#         else:
#             game_round[1] = z
#     return game_rounds
def select_game(game_rounds):
    for game_round in game_rounds:
        if game_round[1] == 'X':
            game_round[1] = 'A'
        elif game_round[1] == 'Y':
            game_round[1] = 'B'
        else:
            game_round[1] = 'C'
    return game_rounds


def calc_score(game_rounds):
    score = 0
    for game_round in game_rounds:
        score += check_selection(game_round)
        score += check_result(game_round)
    return score


def check_selection(game_round):
    score = 3
    if game_round[1] == 'A':
        score = 1
    elif game_round[1] == 'B':
        score = 2
    return score


def check_result(game_round):
    score = 0
    if (game_round[0] == 'A' and game_round[1] == 'B') \
            or (game_round[0] == 'B' and game_round[1] == 'C') \
            or (game_round[0] == 'C' and game_round[1] == 'A'):
        score = 6
    elif game_round[0] == game_round[1]:
        score = 3
    return score


if __name__ == "__main__":
    main()
