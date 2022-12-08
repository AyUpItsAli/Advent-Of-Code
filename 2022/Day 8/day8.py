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


total_visible = 0
for y in range(grid_height):
    for x in range(grid_width):
        tree = grid[y][x]
        if is_visible(tree, x, y):
            total_visible += 1
print(total_visible)
