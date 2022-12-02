def read_input(path):
    octos = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            row = []
            for c in line.strip("\n"):
                row.append(int(c))
                
            octos.append(row)
            line = file.readline()

    return octos
            
octos = read_input("day 11.txt")
print("Initial")
for row in octos:
    print(row)
print()

def get_neighbours(r, c):
    neighbours = []

    # North, South, East, West
    if r != 0:
        # North
        neighbours.append([r-1, c])
    if c != len(octos[r]) - 1:
        # East
        neighbours.append([r, c+1])
    if r != len(octos) - 1:
        # South
        neighbours.append([r+1, c])
    if c != 0:
        # West
        neighbours.append([r, c-1])
        
    # Diagonals
    if r != 0 and c != 0:
        # North West
        neighbours.append([r-1, c-1])
    if r != 0 and c != len(octos[r]) - 1:
        # North East
        neighbours.append([r-1, c+1])
    if r != len(octos) - 1 and c != len(octos[r]) - 1:
        # South East
        neighbours.append([r+1, c+1])
    if r != len(octos) - 1 and c != 0:
        # South West
        neighbours.append([r+1, c-1])
    
    return neighbours
    
total_flashes = 0
for step in range(100):
    for r in range(len(octos)):
        row = octos[r]
        for c in range(len(row)):
            octos[r][c] += 1
    
    print("Step {} Increase".format(step+1))
    for row in octos:
        print(row)
    print()
    
    # A list of octopuses that flashed, this step
    flashed = []

    need_to_flash = False
    for row in octos:
        if need_to_flash: break
        
        for energy in row:
            if energy > 9:
                need_to_flash = True
                break

    print("Need to Flash: {}\n".format(need_to_flash))

    while need_to_flash:
        for r in range(len(octos)):
            row = octos[r]
            for c in range(len(row)):
                energy = octos[r][c]

                # Those that need to flash do so
                # Unless they have already flashed this step
                if energy > 9 and [r, c] not in flashed:
                    flashed.append([r, c])

                    # Add 1 to all neighbours
                    my_neighbours = get_neighbours(r, c)
                    for n in my_neighbours:
                        octos[n[0]][n[1]] += 1
                    
                    print("Flashed {}".format([r, c]))
                    for row in octos:
                        print(row)
                    print()
        
        need_to_flash = False
        for r in range(len(octos)):
            if need_to_flash: break

            row = octos[r]
            for c in range(len(row)):
                energy = octos[r][c]

                if energy > 9 and [r, c] not in flashed:
                    need_to_flash = True
                    break
        
        print("Need to Flash: {}\n".format(need_to_flash))
    
    # After all the flashing stops,
    # We need to set all of the octos that flashed to 0
    for o in flashed:
        octos[o[0]][o[1]] = 0

    total_flashes += len(flashed)
    
    print("End of Step {}".format(step+1))
    for row in octos:
        print(row)
    print()

print("Total Flashes: {}".format(total_flashes))