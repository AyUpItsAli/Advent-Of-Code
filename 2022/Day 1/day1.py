def read_input():
    out = []
    with open("day1input.txt", "r") as file:
        line = file.readline()
        elf = []
        while line:
            if line != "\n":
                elf.append(int(line.strip("\n")))
            else:
                out.append(elf)
                elf = []
            line = file.readline()
    return out


calories = read_input()

totals = []
for elf in calories:
    total = 0
    for food in elf:
        total += food
    totals.append(total)
totals.sort(reverse=True)

# Part 1
print(totals[0])
# Part 2
print(totals[0] + totals[1] + totals[2])
