def read_input(path):
    segments = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            segment = []
            for p in line.strip("\n").split(" -> "):
                point = []
                for t in p.split(","):
                    point.append(int(t))
                segment.append(point)

            segments.append(segment)
            line = file.readline()

    lines = []
    for segment in segments:
        x1, y1 = segment[0][0], segment[0][1]
        x2, y2 = segment[1][0], segment[1][1]

        # Only horizontal lines
        points = []
        if x1 == x2:
            step = 1
            if (y2 - y1) < 0: step = -1
            for y in range(y1, y2 + step, step):
                points.append([x1, y])
        elif y1 == y2:
            step = 1
            if (x2 - x1) < 0: step = -1
            for x in range(x1, x2 + step, step):
                points.append([x, y1])
        
        lines.append(points)

    return lines

grid = []
for r in range(1000):
    row = []
    for c in range(1000):
        row.append(0)
    grid.append(row)

lines = read_input("Day 5/day 5.txt")

for line in lines:
    for point in line:
        x = point[0]
        y = point[1]
        grid[y][x] += 1

count = 0
for row in grid:
    row_count = 0
    for n in row:
        if n >= 2:
            row_count += 1
    count += row_count

print(count)
