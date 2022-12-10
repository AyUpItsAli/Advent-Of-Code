def read_input():
    out = []
    with open("day10input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                instruction = list(line.strip("\n").split(" "))
                if len(instruction) > 1:
                    instruction[1] = int(instruction[1])
                out.append(instruction)
            line = file.readline()
    return out


# OPERATIONS
NOOP = "noop"
PROCESS_ADDX = "process addx"
ADDX = "addx"


# CPU
op_queue = []
cycle = 0
X = 1
operations = read_input()


# CRT Variables
CRT_WIDTH = 40
CRT_HEIGHT = 6
SPRITE_WIDTH = 3
BLANK = "X"
DARK = " "
LIT = "#"


def setup_crt_screen() -> list:
    screen = []
    for y in range(CRT_HEIGHT):
        screen.append([BLANK] * CRT_WIDTH)
    return screen


# CRT
crt_screen = setup_crt_screen()
draw_x_pos = 0
draw_y_pos = 0


def add_next_operation():
    if not operations:
        return
    op = operations.pop(0)
    if op[0] == NOOP:
        op_queue.append(op)
    elif op[0] == ADDX:
        process_op = [PROCESS_ADDX]
        op_queue.extend([process_op, op])


def process_next_operation():
    global X
    if not op_queue:
        return
    op = op_queue.pop(0)
    if op[0] == ADDX:
        value = op[1]
        X += value


def draw_next_pos():
    crt_screen[draw_y_pos][draw_x_pos] = LIT if draw_x_pos in [X - 1, X, X + 1] else DARK


def display_crt_screen():
    for row in crt_screen:
        string = ""
        for x in row:
            string += x
        print(string)


add_next_operation()
while op_queue:
    # Start of cycle
    cycle += 1
    # During cycle
    draw_next_pos()
    # End of cycle
    process_next_operation()
    add_next_operation()
    draw_x_pos += 1
    if draw_x_pos % CRT_WIDTH == 0:
        draw_x_pos = 0  # Reset X pos
        draw_y_pos += 1  # Increase Y pos

display_crt_screen()
