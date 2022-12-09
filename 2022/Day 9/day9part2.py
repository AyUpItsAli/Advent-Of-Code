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
KNOTS = [HEAD.copy() for i in range(9)]
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
    return [pos_to[0] - pos_from[0], pos_to[1] - pos_from[1]]


def get_magnitude(vector: list) -> float:
    return int(math.sqrt(vector[0]**2 + vector[1]**2))


# "knot" follows "leader"
def move_knot(knot: list, leader: list) -> bool:
    displacement = get_displacement(knot, leader)
    distance = get_magnitude(displacement)
    if distance > 1:
        if displacement[1] == 0:
            sign = 1 if displacement[0] > 0 else -1
            knot[0] += sign
        elif displacement[0] == 0:
            sign = 1 if displacement[1] > 0 else -1
            knot[1] += sign
        else:
            sign = 1 if displacement[0] > 0 else -1
            knot[0] += sign
            sign = 1 if displacement[1] > 0 else -1
            knot[1] += sign
        return True
    return False


visited = [HEAD.copy()]
for move in moves:
    direction = move[0]
    steps = int(move[1])
    for _ in range(steps):
        move_head(direction)
        for k in range(len(KNOTS)):
            knot = KNOTS[k]
            leader = HEAD if k == 0 else KNOTS[k-1]
            if move_knot(knot, leader) and k == len(KNOTS)-1 and knot not in visited:
                visited.append(knot.copy())
print(len(visited))
