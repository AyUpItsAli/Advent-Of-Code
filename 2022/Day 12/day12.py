from yaspin import yaspin
from yaspin.spinners import Spinners


def read_input():
    out = []
    with open("day12input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                row = list(line.strip("\n"))
                out.append(row)
            line = file.readline()
    return out


height_map = read_input()
height = len(height_map)
width = len(height_map[0])


def is_out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or x >= width or y < 0 or y >= height


def get_elevation(x: int, y: int) -> str:
    if is_out_of_bounds(x, y): return ""
    elevation = height_map[y][x]
    if elevation == "S":
        return "a"
    if elevation == "E":
        return "z"
    return elevation


def can_move(from_pos: list, to_pos: list) -> bool:
    to_x = to_pos[0]
    to_y = to_pos[1]
    to_elevation = get_elevation(to_x, to_y)
    if to_elevation == "":
        return False
    from_x = from_pos[0]
    from_y = from_pos[1]
    from_elevation = get_elevation(from_x, from_y)
    return ord(to_elevation) <= ord(from_elevation) + 1


def get_shortest_distance(start: list, end: list) -> int:
    queue = [start]
    visited = [start]
    distance = 0
    while queue and end not in queue:
        distance += 1
        neighbours = []
        for pos in queue:
            x = pos[0]
            y = pos[1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if abs(i) > 0 and abs(j) > 0:  # Only up, down, left and right (no diagonals).
                        continue
                    neighbour = [x+j, y+i]
                    if can_move(pos, neighbour) and neighbour not in visited:
                        neighbours.append(neighbour)
                        visited.append(neighbour)
        queue = neighbours
    return distance if end in queue else -1  # -1 if end was not reached


S = [0, 0]
E = [0, 0]
with yaspin(text="[Part 1]", side="right", spinner=Spinners.material, timer=True) as spinner:
    for y in range(height):
        for x in range(width):
            if height_map[y][x] == "S":
                S = [x, y]
            elif height_map[y][x] == "E":
                E = [x, y]
    distance = get_shortest_distance(S, E)
    spinner.ok(text=f"Result: {distance}")


with yaspin(text="[Part 2]", side="right", spinner=Spinners.material, timer=True) as spinner:
    for y in range(height):
        for x in range(width):
            if height_map[y][x] != "S" and height_map[y][x] == "a":
                pos = [x, y]
                new_distance = get_shortest_distance(pos, E)
                if new_distance != -1 and new_distance < distance:
                    distance = new_distance
    spinner.ok(text=f"Result: {distance}")
