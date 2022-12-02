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
    if code == "A":
        return ROCK
    elif code == "B":
        return PAPER
    elif code == "C":
        return SCISSORS


def get_result(code) -> str:
    if code == "X":
        return LOSS
    elif code == "Y":
        return DRAW
    elif code == "Z":
        return WIN


def get_my_shape(their_shape: int, result) -> int:
    if result == LOSS:
        return (their_shape + 1) % 3
    elif result == WIN:
        return (their_shape - 1) % 3
    return their_shape


turns = read_input()
total_score = 0
for turn in turns:
    score = 0

    their_shape = get_shape(turn[0])
    result = get_result(turn[1])
    if result == DRAW:
        score += 3
    elif result == WIN:
        score += 6

    my_shape = get_my_shape(their_shape, result)
    if my_shape == ROCK:
        score += 1
    elif my_shape == PAPER:
        score += 2
    elif my_shape == SCISSORS:
        score += 3

    total_score += score
print(total_score)
