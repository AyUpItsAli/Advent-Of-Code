from collections import Counter

def read_input(path):
    population = []
    with open(path, "r") as file:
        line = file.readline()
        for n in line.strip("\n").split(","):
            population.append(int(n))
    return population

population = dict(Counter(read_input("day 6.txt")))

for d in range(256):
    new_population = {}
    for age in population:
        if age > 0:
            if (age-1) in new_population: new_population[age-1] += population[age]
            else: new_population[age-1] = population[age]
        elif age == 0:
            if 6 in new_population: new_population[6] += population[age]
            else: new_population[6] = population[age]

            new_population[8] = population[age]

    population = new_population
    print("After Day {}: {}".format(d+1, population))

count = 0
for age in population:
    count += population[age]
print(count)