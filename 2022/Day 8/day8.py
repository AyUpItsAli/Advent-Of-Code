def read_input():
    out = []
    with open("day8input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                row = [int(x) for x in line.strip("\n")]
                out.append(row)
            line = file.readline()
    return out


grid = read_input()
grid_height = len(grid)
grid_width = len(grid[0])


def is_edge(x: int, y: int) -> bool:
    return x == 0 or y == 0 or x == grid_width-1 or y == grid_height-1


def is_visible(tree: int, x: int, y: int) -> bool:
    if is_edge(x, y):
        return True

    visible_left = True
    for x_offset in range(-x, 0):
        neighbour = grid[y][x + x_offset]
        if neighbour >= tree:
            visible_left = False

    visible_right = True
    for x_offset in range(1, grid_width-x):
        neighbour = grid[y][x + x_offset]
        if neighbour >= tree:
            visible_right = False

    visible_up = True
    for y_offset in range(-y, 0):
        neighbour = grid[y + y_offset][x]
        if neighbour >= tree:
            visible_up = False

    visible_down = True
    for y_offset in range(1, grid_height - y):
        neighbour = grid[y + y_offset][x]
        if neighbour >= tree:
            visible_down = False

    return visible_left or visible_right or visible_up or visible_down


def is_out_of_bounds(x: int, y: int) -> bool:
    return x < 0 or y < 0 or x >= grid_width or y >= grid_height


def get_scenic_score(tree: int, x: int, y: int) -> int:
    distance_left = 0
    for x_offset in range(-1, -x-1, -1):
        if is_out_of_bounds(x + x_offset, y):
            break
        distance_left += 1
        neighbour = grid[y][x + x_offset]
        if neighbour >= tree:
            break

    distance_right = 0
    for x_offset in range(1, grid_width - x):
        if is_out_of_bounds(x + x_offset, y):
            break
        distance_right += 1
        neighbour = grid[y][x + x_offset]
        if neighbour >= tree:
            break

    distance_up = 0
    for y_offset in range(-1, -y-1, -1):
        if is_out_of_bounds(x, y + y_offset):
            break
        distance_up += 1
        neighbour = grid[y + y_offset][x]
        if neighbour >= tree:
            break

    distance_down = 0
    for y_offset in range(1, grid_height - y):
        if is_out_of_bounds(x, y + y_offset):
            break
        distance_down += 1
        neighbour = grid[y + y_offset][x]
        if neighbour >= tree:
            break

    return distance_left * distance_right * distance_up * distance_down


# Part 1
total_visible = 0
for y in range(grid_height):
    for x in range(grid_width):
        tree = grid[y][x]
        if is_visible(tree, x, y):
            total_visible += 1
print(total_visible)

# Part 2
scores = []
for y in range(grid_height):
    for x in range(grid_width):
        tree = grid[y][x]
        scores.append(get_scenic_score(tree, x, y))
scores.sort(reverse=True)
print(scores[0])
