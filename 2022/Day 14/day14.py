from yaspin import yaspin
from yaspin.spinners import Spinners


AIR = "."
ROCK = "#"
SAND = "o"
SAND_SOURCE = [500, 0]
SOLID_TILES = [ROCK, SAND]
# Number of tiles added to the left and right of the grid.
# Without this, the sand can get bunched up on the right side of the grid, treating it as a solid wall.
PADDING = 200


def read_structures() -> list[list[list[int]]]:
    out = []
    with open("day14input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                structure = line.strip("\n").split(" -> ")
                out.append([list(map(int, point.split(","))) for point in structure])
            line = file.readline()
    return out


def setup_cave(structures: list[list[list[int]]]):
    height = 1
    width = 1
    min_x = structures[0][0][0]
    for structure in structures:
        for point in structure:
            if (point[1] + 1) > height:
                height = point[1] + 1
            if (point[0] + 1) > width:
                width = point[0] + 1
            if point[0] < min_x:
                min_x = point[0]

    max_y = height-1
    floor = max_y + 2
    height += 2
    width += PADDING  # Add some padding, to allow the sand to exceed the total width of the rock STRUCTURES
    min_x -= PADDING  # Padding added to min_x only effects the draw_cave() function. It has no other function.

    # Initialise cave
    cave = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(AIR)
        cave.append(row)

    # Place rock structures
    for structure in structures:
        for i, point in enumerate(structure[:-1]):
            next_point = structure[i + 1]
            if point[0] == next_point[0]:
                x = point[0]
                step = 1 if next_point[1] > point[1] else -1
                for y in range(point[1], next_point[1] + step, step):
                    cave[y][x] = ROCK
            elif point[1] == next_point[1]:
                y = point[1]
                step = 1 if next_point[0] > point[0] else -1
                for x in range(point[0], next_point[0] + step, step):
                    cave[y][x] = ROCK

    # Place floor
    for x in range(min_x, width):
        cave[floor][x] = ROCK

    return cave, height, width, min_x, max_y, floor


STRUCTURES = read_structures()
CAVE, HEIGHT, WIDTH, MIN_X, MAX_Y, FLOOR = setup_cave(STRUCTURES)
SAND_IN_MOTION = []  # List of sand positions that are still moving


# Adds a new sand tile at SAND_SOURCE pos
def add_sand():
    if SAND_SOURCE in SAND_IN_MOTION:  # If start pos occupied, do nothing. Unlikely, but validation makes me happy :)
        return
    CAVE[SAND_SOURCE[1]][SAND_SOURCE[0]] = SAND
    SAND_IN_MOTION.append(SAND_SOURCE.copy())


def out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT


# Movement function for Part 1:
# Returns true if sand in motion is falling into the void
def move_sand_until_void() -> bool:
    sand_at_rest = []  # List of sand positions that should stop moving
    sand: list
    for s, sand in enumerate(SAND_IN_MOTION):
        if sand[1] == MAX_Y:
            return True
        old_pos = sand.copy()
        new_pos = None
        new_pos_options = [
            [sand[0], sand[1] + 1],  # Directly down
            [sand[0] - 1, sand[1] + 1],  # Then try down and to the left
            [sand[0] + 1, sand[1] + 1]  # Then try down and to the right
        ]
        for pos in new_pos_options:
            if out_of_bounds(pos[0], pos[1]):
                continue
            if CAVE[pos[1]][pos[0]] in SOLID_TILES:
                continue
            new_pos = pos
            break
        if new_pos:
            CAVE[new_pos[1]][new_pos[0]] = SAND
            CAVE[old_pos[1]][old_pos[0]] = AIR
            SAND_IN_MOTION[s] = new_pos
        else:
            sand_at_rest.append(sand)

    # Remove sand that has come to rest from the list of sand in motion
    for sand in sand_at_rest:
        SAND_IN_MOTION.remove(sand)

    return False


# Movement function for Part 2:
# Returns true if sand source (SAND_SOURCE) is blocked
def move_sand_until_source_blocked() -> bool:
    sand_at_rest = []  # List of sand positions that should stop moving
    sand: list
    for s, sand in enumerate(SAND_IN_MOTION):
        old_pos = sand.copy()
        new_pos = None
        new_pos_options = [
            [sand[0], sand[1] + 1],  # Directly down
            [sand[0] - 1, sand[1] + 1],  # Then try down and to the left
            [sand[0] + 1, sand[1] + 1]  # Then try down and to the right
        ]
        for pos in new_pos_options:
            if out_of_bounds(pos[0], pos[1]):
                continue
            if CAVE[pos[1]][pos[0]] in SOLID_TILES:
                continue
            new_pos = pos
            break
        if new_pos:
            CAVE[new_pos[1]][new_pos[0]] = SAND
            CAVE[old_pos[1]][old_pos[0]] = AIR
            SAND_IN_MOTION[s] = new_pos
        else:
            sand_at_rest.append(sand)

    # Remove sand that has come to rest from the list of sand in motion
    for sand in sand_at_rest:
        SAND_IN_MOTION.remove(sand)
        if sand == SAND_SOURCE:  # If at rest AND at the starting point, no more sand can fall
            return True

    return False


def draw_cave(write: bool = False):
    text = ""
    for row in CAVE:
        string = "".join(row[MIN_X:])
        text += string + "\n"
    if write:
        with open("output.txt", "w") as file:
            file.write(text)
    print(text)


def get_num_sand_at_rest_after_falling_into_void() -> int:
    global CAVE, HEIGHT, WIDTH, MIN_X, MAX_Y, FLOOR, SAND_IN_MOTION
    CAVE, HEIGHT, WIDTH, MIN_X, MAX_Y, FLOOR = setup_cave(STRUCTURES)
    SAND_IN_MOTION = []

    num_at_rest = 0
    fallen_in_void = False
    while not fallen_in_void:
        if SAND_IN_MOTION:
            num_in_motion_before = len(SAND_IN_MOTION)
            fallen_in_void = move_sand_until_void()
            num_at_rest += num_in_motion_before - len(SAND_IN_MOTION)
        else:
            add_sand()
    draw_cave()
    return num_at_rest


with yaspin(text="[Part 1]", side="right", spinner=Spinners.material, timer=True) as spinner:
    result = get_num_sand_at_rest_after_falling_into_void()
    spinner.ok(text=f"Result: {result}")


def get_num_sand_at_rest_after_source_blocked() -> int:
    global CAVE, HEIGHT, WIDTH, MIN_X, MAX_Y, FLOOR, SAND_IN_MOTION
    CAVE, HEIGHT, WIDTH, MIN_X, MAX_Y, FLOOR = setup_cave(STRUCTURES)
    SAND_IN_MOTION = []

    num_at_rest = 0
    source_blocked = False
    while not source_blocked:
        if SAND_IN_MOTION:
            num_in_motion_before = len(SAND_IN_MOTION)
            source_blocked = move_sand_until_source_blocked()
            num_at_rest += num_in_motion_before - len(SAND_IN_MOTION)
        else:
            add_sand()
    draw_cave(True)
    return num_at_rest


with yaspin(text="[Part 2]", side="right", spinner=Spinners.material, timer=True) as spinner:
    result = get_num_sand_at_rest_after_source_blocked()
    spinner.ok(text=f"Result: {result}")
