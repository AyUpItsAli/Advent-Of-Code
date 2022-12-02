def read_input(path):
    positions = []
    with open(path, "r") as file:
        line = file.readline()
        for pos in line.strip("\n").split(","):
            positions.append(int(pos))

    return positions

positions = read_input("day 7.txt")

biggest = 0
for pos in positions:
    if pos > biggest:
        biggest = pos

lowest_fuel = 0
for align in range(biggest):
    fuel = 0
    for pos in positions:
        fuel += abs(pos - align)

    if align == 0 or fuel < lowest_fuel:
        lowest_fuel = fuel

print(lowest_fuel)