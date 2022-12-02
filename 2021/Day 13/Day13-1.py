def read_input(path):
    points, folds = [], []
    with open(path, "r") as file:

        # Points
        line = file.readline()
        while line != "\n":
            point = []
            for n in line.strip("\n").split(","): point.append(int(n))
            points.append(point)

            line = file.readline()
        
        # Folds
        line = file.readline()
        while line:
            fold = []
            for n in line.strip("\n").strip("fold along ").split("="):
                try: fold.append(int(n))
                except: fold.append(n)
            folds.append(fold)

            line = file.readline()

    return points, folds

points, folds = read_input("day 13.txt")

points.sort(key=lambda x: x[0])
max_x = points[-1][0]

points.sort(key=lambda x: x[1])
max_y = points[-1][1]

page = []
for y in range(max_y + 1):
    row = []
    for x in range(max_x + 1):
        row.append(".")
    page.append(row)

for point in points:
    page[point[1]][point[0]] = "#"

for fold in folds:
    new_page = []

    # Vertical fold
    if fold[0] == "x":
        fold_x = fold[1]

        for y in range(len(page)):
            row = []
            for x in range(fold_x + 1):
                row.append(".")
            new_page.append(row)

        for r in range(len(page)):
            row = page[r]
            for c in range(len(row)):
                point = row[c]
                if point == "#":
                    if c > fold_x:
                        dist = c - fold_x
                        new_page[r][fold_x - dist] = "#"
                    else:
                        new_page[r][c] = "#"
                

    # Horizontal fold
    elif fold[0] == "y":
        fold_y = fold[1]
        
        for y in range(fold_y + 1):
            row = []
            for x in range(len(page[0])):
                row.append(".")
            new_page.append(row)

        for r in range(len(page)):
            row = page[r]
            for c in range(len(row)):
                point = row[c]
                if point == "#":
                    if r > fold_y:
                        dist = r - fold_y
                        new_page[fold_y - dist][c] = "#"
                    else:
                        new_page[r][c] = "#"

    page = new_page
    break

total = 0
for row in page:
    for point in row:
        if point == "#": total += 1

print(total)