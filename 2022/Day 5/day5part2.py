def read_input():
    stacks = {}
    steps = []
    with open("day5input.txt", "r") as file:
        # Stacks
        line = file.readline()
        while line != "\n":
            row = line.strip("\n")
            for i in range(0, len(row), 4):
                if row[i] == "[":
                    stack = int(i / 4) + 1
                    crate = row[i + 1]
                    if stack in stacks:
                        # Crates are added from top to bottom. This is wrong and will be handled later...
                        stacks[stack].append(crate)
                    else:
                        stacks[stack] = [crate]
            line = file.readline()

        # Reverse the stacks, as the crates were added from top to bottom, not bottom to top
        for stack in stacks:
            stacks[stack].reverse()

        # Steps
        line = file.readline()
        while line:
            if line != "\n":
                step =[]
                for x in line.strip("\n").replace("move ", "").replace("from ", "").replace("to ", "").split(" "):
                    step.append(int(x))
                steps.append(step)
            line = file.readline()
    return stacks, steps


stacks, steps = read_input()

# Carry out procedure steps
for step in steps:
    num_crates = step[0]
    from_stack = step[1]
    to_stack = step[2]
    removed = []
    for _ in range(num_crates):
        removed.append(stacks[from_stack].pop())  # Append crates to intermediate list
    removed.reverse()  # Reverse the list
    for crate in removed:
        stacks[to_stack].append(crate)  # Add the crates in reverse, to maintain original order

# Print final stacks and final message
message = ""
for stack in sorted(stacks):
    print("Stack {}: {}".format(stack, stacks[stack]))
    if stacks[stack]:
        message += stacks[stack].pop()
print(message)
