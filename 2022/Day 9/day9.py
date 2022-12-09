import math


def read_input():
    out = []
    with open("day9input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                move = list(line.strip("\n").split(" "))
                move[1] = int(move[1])
                out.append(move)
            line = file.readline()
    return out


LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"


def move_head(head: list, direction: str):
    if direction == LEFT:
        head[0] -= 1
    elif direction == RIGHT:
        head[0] += 1
    elif direction == UP:
        head[1] += 1
    elif direction == DOWN:
        head[1] -= 1


def get_displacement(pos_from: list, pos_to: list) -> list:
    return [pos_to[0] - pos_from[0], pos_to[1] - pos_from[1]]


def get_magnitude(vector: list) -> float:
    return math.sqrt(vector[0]**2 + vector[1]**2)


# Knot follows leader
# Returns whether the knot moved or not
def move_knot(knot: list, leader: list) -> bool:
    displacement = get_displacement(knot, leader)
    distance: float = get_magnitude(displacement)
    if int(distance) > 1:
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


def get_num_positions_visited_by_tail(moves: list, num_knots: int = 2) -> int:
    knots = [[0, 0].copy() for _ in range(num_knots)]
    head = knots[0]
    tail = knots[-1]

    visited = [tail.copy()]
    for move in moves:
        direction = move[0]
        steps = move[1]
        for _ in range(steps):
            move_head(head, direction)
            for k in range(num_knots):
                knot = knots[k]
                leader = head if k == 0 else knots[k-1]
                if move_knot(knot, leader) and knot is tail and knot not in visited:
                    visited.append(knot.copy())
    return len(visited)


moves = read_input()

# Part 1
print(get_num_positions_visited_by_tail(moves))
# Part 2
print(get_num_positions_visited_by_tail(moves, 10))
