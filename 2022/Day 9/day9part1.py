import math


def read_input():
    out = []
    with open("day9input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                out.append(line.strip("\n").split(" "))
            line = file.readline()
    return out


LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

HEAD = [0, 0]
TAIL = [0, 0]
moves = read_input()


def move_head(direction: str):
    if direction == LEFT:
        HEAD[0] -= 1
    elif direction == RIGHT:
        HEAD[0] += 1
    elif direction == UP:
        HEAD[1] += 1
    elif direction == DOWN:
        HEAD[1] -= 1


def get_displacement(pos_from: list, pos_to: list) -> list:
    displacement = [0, 0]
    displacement[0] = pos_to[0] - pos_from[0]
    displacement[1] = pos_to[1] - pos_from[1]
    return displacement


def get_magnitude(vector: list) -> float:
    square_sum = (vector[0]**2) + (vector[1]**2)
    return int(math.sqrt(square_sum))


# TAIL follows HEAD
def move_tail() -> bool:
    displacement = get_displacement(TAIL, HEAD)
    distance = get_magnitude(displacement)
    if distance > 1:
        if displacement[1] == 0:
            sign = 1 if displacement[0] > 0 else -1
            TAIL[0] += sign
        elif displacement[0] == 0:
            sign = 1 if displacement[1] > 0 else -1
            TAIL[1] += sign
        else:
            sign = 1 if displacement[0] > 0 else -1
            TAIL[0] += sign
            sign = 1 if displacement[1] > 0 else -1
            TAIL[1] += sign
        return True
    return False


visited = [TAIL.copy()]
for move in moves:
    direction = move[0]
    steps = int(move[1])
    for s in range(steps):
        move_head(direction)
        if move_tail() and TAIL not in visited:
            visited.append(TAIL.copy())
print(len(visited))
