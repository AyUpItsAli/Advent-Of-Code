def read_input(path):
    height_map = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            row = []
            for n in line.strip("\n"):
                row.append(int(n))
            height_map.append(row)

            line = file.readline()
    
    return height_map

height_map = read_input("day 9.txt")

risk_total = 0
for r in range(len(height_map)):
    row = height_map[r]
    for c in range(len(row)):
        height = row[c]
        
        neighbours = []
        if r != 0: neighbours.append(height_map[r-1][c])
        if c != len(row) - 1: neighbours.append(height_map[r][c+1])
        if r != len(height_map) - 1: neighbours.append(height_map[r+1][c])
        if c != 0: neighbours.append(height_map[r][c-1])

        low_point = True
        for n in neighbours:
            if n <= height:
                low_point = False

        if low_point:
            risk_total += (height + 1)

print(risk_total)