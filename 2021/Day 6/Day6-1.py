def read_input(path):
    population = []
    with open(path, "r") as file:
        line = file.readline()
        for n in line.strip("\n").split(","):
            population.append(int(n))
    return population

population = read_input("day 6.txt")

for d in range(80):
    for i in range(len(population)):
        if population[i] == 0:
            population[i] = 6
            population.append(8)
        else:
            population[i] -= 1

print("Total Population: {}".format(len(population)))