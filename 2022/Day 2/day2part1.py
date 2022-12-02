def read_input():
    out = []
    with open("day2input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                choice = line.strip("\n").split(" ")
                out.append(choice)
            line = file.readline()
    return out


# Rock -> Scissors -> Paper -> Rock -> ...
ROCK = 0
SCISSORS = 1
PAPER = 2

LOSS = "Loss"
DRAW = "Draw"
WIN = "Win"


def get_shape(code) -> int:
    if code in ["A", "X"]:
        return ROCK
    elif code in ["B", "Y"]:
        return PAPER
    elif code in ["C", "Z"]:
        return SCISSORS


def get_result(my_shape: int, their_shape: int) -> str:
    if my_shape == their_shape: return DRAW
    win_shape = (my_shape + 1) % 3
    if their_shape == win_shape: return WIN
    return LOSS


turns = read_input()
total_score = 0
for turn in turns:
    score = 0

    my_shape = get_shape(turn[1])
    if my_shape == ROCK:
        score += 1
    elif my_shape == PAPER:
        score += 2
    elif my_shape == SCISSORS:
        score += 3

    their_shape = get_shape(turn[0])
    result = get_result(my_shape, their_shape)
    if result == DRAW:
        score += 3
    elif result == WIN:
        score += 6

    total_score += score
print(total_score)
