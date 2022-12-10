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


NOOP = "noop"
PROCESS_ADDX = "process addx"
ADDX = "addx"


operations = read_input()
op_queue = []
X = 1
cycle = 0


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
    return op


START = 20  # 20...
EVERY = 40  # ...60, 100, 140, 180...
signal_sum = 0

add_next_operation()
while op_queue:
    # Start of cycle
    cycle += 1
    # During cycle
    if (cycle + START) % EVERY == 0:
        signal_sum += X * cycle
    # End of cycle
    process_next_operation()
    add_next_operation()
print(signal_sum)
