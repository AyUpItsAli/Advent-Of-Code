def read_input():
    out = []
    with open("day14input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                structures = line.strip("\n").split(" -> ")
                out.append([list(map(int, structure.split(","))) for structure in structures])
            line = file.readline()
    return out


AIR = "."
ROCK = "#"
SAND = "O"
SAND_START = [500, 0]
SOLID_TILES = [ROCK, SAND]


structures = read_input()


def setup_cave():
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
    out = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(AIR)
        out.append(row)
    return out, height, width, min_x


cave, HEIGHT, WIDTH, MIN_X = setup_cave()


def draw_cave():
    for row in cave:
        print("".join(row[MIN_X-1:]))


def place_structures():
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


place_structures()


# List of positions for sand that is still moving
SAND_IN_MOTION = []


# Adds new sand at SAND_START pos
def produce_sand():
    if SAND_START in SAND_IN_MOTION:  # If start position occupied
        return
    cave[SAND_START[1]][SAND_START[0]] = SAND
    SAND_IN_MOTION.append(SAND_START.copy())
    draw_cave()


def out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT


# Returns the number of sand tiles that have come to rest
def move_sand() -> bool:
    global SAND_IN_MOTION
    global SOLID_TILES
    moving_sand_remaining = []  # List of positions for sand that is still moving after this move

    sand: list
    for sand in SAND_IN_MOTION:
        if sand[1] == HEIGHT-1:
            return True
        old_pos = sand.copy()
        next_pos = None
        for pos in [[sand[0], sand[1] + 1], [sand[0] - 1, sand[1] + 1], [sand[0] + 1, sand[1] + 1]]:
            if out_of_bounds(pos[0], pos[1]):
                continue
            if cave[pos[1]][pos[0]] in SOLID_TILES:
                continue
            next_pos = pos
            break
        if next_pos:
            cave[next_pos[1]][next_pos[0]] = SAND
            cave[old_pos[1]][old_pos[0]] = AIR
            moving_sand_remaining.append(next_pos)
    SAND_IN_MOTION = moving_sand_remaining
    draw_cave()
    return False


num_at_rest = 0
fell_into_abyss = False
cycle = 0
for i in range(3):
    cycle += 1
    produce_sand()
    num_moving_before = len(SAND_IN_MOTION)
    while SAND_IN_MOTION:
        fell_into_abyss = move_sand()
        if fell_into_abyss:
            break
    num_at_rest += num_moving_before - len(SAND_IN_MOTION)

# 878 is too high
print(num_at_rest)
