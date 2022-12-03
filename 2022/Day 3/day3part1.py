import string


def read_input():
    out = []
    with open("day3input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                out.append(line.strip("\n"))
            line = file.readline()
    return out


def get_priority(item: str) -> int:
    lowercase_index = string.ascii_lowercase.index(item.lower())
    if item.isupper():
        return lowercase_index + 27
    return lowercase_index + 1


rucksacks = read_input()
priority_sum = 0
for rucksack in rucksacks:
    compartment1 = rucksack[0:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):len(rucksack)]
    misplaced_item = None
    for item in compartment1:
        if item in compartment2:
            misplaced_item = item
            break
    priority_sum += get_priority(misplaced_item)
print(priority_sum)
