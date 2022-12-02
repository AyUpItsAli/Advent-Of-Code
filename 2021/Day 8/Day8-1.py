def read_input(path):
    entries = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            entry = []
            for n in line.strip("\n").split(" | "):
                entry.append(n.split(" "))
            entries.append(entry)
            line = file.readline()

    return entries

entries = read_input("day 8.txt")

count = 0
for entry in entries:
    for digit in entry[1]:
        length = len(digit)
        if length == 2 or length == 3 or length == 4 or length == 7:
            count += 1
print(count)