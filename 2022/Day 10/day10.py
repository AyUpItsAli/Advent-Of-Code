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
ADDX = "addx"
PROCESS_ADDX = "process addx"


operations = read_input()
op_queue = []
X = 1
cycle = 0


def add_next_operation():
    if not operations:
        return
    next_op = operations.pop(0)
    if next_op[0] == NOOP:
        op_queue.append(next_op)
    elif next_op[0] == ADDX:
        process = [PROCESS_ADDX]
        op_queue.extend([process, next_op])


def process_next_operation():
    global X

    if not op_queue:
        return
    next_op = op_queue.pop(0)
    if next_op[0] == ADDX:
        value = next_op[1]
        X += value
    return next_op


START = 20
EVERY = 40
signal_sum = 0

add_next_operation()
while op_queue:
    # Start of cycle
    cycle += 1
    # During cycle
    if (cycle + START) % EVERY == 0:
        signal_sum += X * cycle
    # End of cycle
    next_op = process_next_operation()
    add_next_operation()
print(signal_sum)
