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

# Number of tiles added to the width of the grid.
# Without this, the sand gets bunched up on the side of the grid, treating it as a solid wall.
PADDING = 10


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

    width += PADDING  # Add some padding, to allow the sand to exceed the total width of the rock structures

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
            else:
                # If we get here, then some structures consist of non-straight lines
                print("uh oh! Structures contain non-straight lines!")


# List of sand positions that are still moving
sand_in_motion = []


# Adds a new sand tile at SAND_START pos
def add_sand():
    if SAND_START in sand_in_motion:  # If start pos occupied, do nothing. Unlikely, but validation makes me happy :)
        return
    cave[SAND_START[1]][SAND_START[0]] = SAND
    sand_in_motion.append(SAND_START.copy())


def out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT


# Returns true if sand in motion is falling into the void
def move_sand() -> bool:
    sand_at_rest = []  # List of sand positions that should stop moving
    sand: list
    for s, sand in enumerate(sand_in_motion):
        if sand[1] == HEIGHT-1:
            print(f"{sand} is falling into the void!")
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
            if cave[pos[1]][pos[0]] in SOLID_TILES:
                continue
            new_pos = pos
            break
        if new_pos:
            cave[new_pos[1]][new_pos[0]] = SAND
            cave[old_pos[1]][old_pos[0]] = AIR
            sand_in_motion[s] = new_pos
        else:
            sand_at_rest.append(sand)

    # Remove sand that has come to rest from the list of sand in motion
    for sand in sand_at_rest:
        sand_in_motion.remove(sand)

    return False


place_structures()
num_at_rest = 0
fallen_into_void = False
while not fallen_into_void:
    if sand_in_motion:
        num_in_motion_before = len(sand_in_motion)
        fallen_into_void = move_sand()
        num_at_rest += num_in_motion_before - len(sand_in_motion)
    else:
        add_sand()
draw_cave()
print(num_at_rest)
