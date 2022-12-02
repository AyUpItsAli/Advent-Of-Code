def read_input(file_path):
    neighbours = {}
    with open(file_path, "r") as file:
        line = file.readline()
        while line:

            # A list that represents the path between two caves
            path = line.strip("\n").split("-")

            # Add 2nd cave of the connection to list of neighbours for 1st cave
            if path[0] in neighbours:
                n_list = neighbours[path[0]]
                n_list.append(path[1])
                neighbours[path[0]] = n_list
            else:
                neighbours[path[0]] = [path[1]]
            
            # Add 1st cave of the connection to list of neighbours for 2nd cave
            if path[1] in neighbours:
                n_list = neighbours[path[1]]
                n_list.append(path[0])
                neighbours[path[1]] = n_list
            else:
                neighbours[path[1]] = [path[0]]
            
            line = file.readline()
    
    return neighbours

def move(route):
    global routes

    # If we are not at the end, continue
    if route[-1] != "end":

        # Loop through all of the neighbours of the current cave we are in
        for next_cave in neighbours[route[-1]]:
            
            # We cannot go back to the start cave, so skip this if it is the start cave
            if next_cave == "start":
                continue

            # If this is a big cave, then we can move to it
            # If this is a small cave and we have not visited it yet, then we can move to it
            if (next_cave.upper() == next_cave) or (next_cave not in route):

                # Add the cave to the route
                route.append(next_cave)

                # Continue the route from this new location
                move(route)

                # Once the recursive function returns, we remove the last cave,
                # and continue checking the rest of our neighbours
                route.pop()
        
        # Once we have checked all our neighbours this function returns

        # After all functions return, the inital function returns and we print our result
    
    else:
        # If this route has ended, then we have found a new route
        # so increment our counter
        routes += 1

# Dictionary of String keys (caves) and List values (neighbours of that cave)
neighbours = read_input("day 12.txt")
# Counter. Number of routes from start to end.
routes = 0

# Starting state for route 1
start = ["start"]
# Begin recursion
move(start)

print(routes)