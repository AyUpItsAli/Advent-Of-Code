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


CRT_HEIGHT = 6
CRT_WIDTH = 40
SPRITE_WIDTH = 3
BLANK = " "
DARK = "."
LIT = "#"


def setup_crt_screen():
    screen = []
    for y in range(CRT_HEIGHT):
        row = []
        for x in range(CRT_WIDTH):
            row.append(BLANK)
        screen.append(row)
    return screen


NOOP = "noop"
PROCESS_ADDX = "process addx"
ADDX = "addx"


operations = read_input()
op_queue = []
X = 1
cycle = 0
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
        #print("ADDX {}, X = {}".format(value, X))
    return op


def draw_next_pos():
    crt_screen[draw_y_pos][draw_x_pos] = LIT if draw_x_pos in [X - 1, X, X + 1] else DARK


START = 20
EVERY = 40
signal_sum = 0

add_next_operation()
while op_queue:
    # Start of cycle
    cycle += 1
    #print("Cycle: {}, Queue: {}".format(cycle, op_queue))
    # During cycle
    if (cycle + START) % EVERY == 0:
        signal_sum += X * cycle
    #print("Drawing: {}, {}".format(draw_x_pos, draw_y_pos))
    draw_next_pos()
    #print(crt_screen[draw_y_pos])
    # End of cycle
    process_next_operation()
    #print("Sprite pos: {}, {}".format(X, draw_y_pos))
    add_next_operation()
    draw_x_pos += 1
    if draw_x_pos % CRT_WIDTH == 0:
        draw_x_pos = 0  # Reset X pos
        draw_y_pos += 1  # Increase Y pos
    #print()
#print(signal_sum)

for row in crt_screen:
    string = ""
    for x in row:
        string += x
    print(string)
