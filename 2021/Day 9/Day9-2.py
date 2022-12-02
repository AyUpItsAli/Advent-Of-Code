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

def get_new_neighbours(r, c):
    neighbours = []
    
    # Again, we only care about locations that are not 9 and not None
    if r != 0:
        loc = height_map[r-1][c]
        if loc != 9 and loc != None:
            neighbours.append([r-1, c])
            height_map[r-1][c] = None
    if c != len(row) - 1:
        loc = height_map[r][c+1]
        if loc != 9 and loc != None:
            neighbours.append([r, c+1])
            height_map[r][c+1] = None
    if r != len(height_map) - 1:
        loc = height_map[r+1][c]
        if loc != 9 and loc != None:
            neighbours.append([r+1, c])
            height_map[r+1][c] = None
    if c != 0:
        loc = height_map[r][c-1]
        if loc != 9 and loc != None:
            neighbours.append([r, c-1])
            height_map[r][c-1] = None
    
    return neighbours

basins = []
for r in range(len(height_map)):
    row = height_map[r]
    for c in range(len(row)):
        height = row[c]
        
        # Look for a NEW basin
        # This means, any location that isn't as high as 9 and is also not None,
        # because None, in this case, means we have already dealt with it
        if height != 9 and height != None:
            # Set this new location to None, as we are about to deal with it
            height_map[r][c] = None
            
            # We want to keep track of the members of this basin.
            # Let's start by getting this location's immediate neighbours (up to 4)
            members = get_new_neighbours(r, c)
            # Set new_members to the neighbours we just retrieved
            new_members = members

            # While this basin has new members (ie: there are more locations in this basin)...
            # ...we continue looking for more members
            while new_members != []:
                # Reset new_members to a blank list, to test if we have any more
                new_members = []

                # For each of the current members of this basin,
                # Add any NEW neighbours to the new_members list
                # That means, any locations that we haven't already dealt with
                for member in members:
                    for new_m in get_new_neighbours(member[0], member[1]):
                        new_members.append(new_m)
                
                # Don't forget to add the new_members to the main members list
                for new_m in new_members:
                    members.append(new_m)
            
            # Don't forget to add 1 for the starting location!
            basin_size = len(members) + 1
            basins.append(basin_size)

# Sort to find the top 3 basin sizes
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])