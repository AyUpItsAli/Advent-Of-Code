import string


def read_input():
    out = []
    with open("day3input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                group = []
                for i in range(3):
                    group.append(line.strip("\n"))
                    line = file.readline()
                out.append(group)
            else:
                line = file.readline()
    return out


def get_priority(item: str) -> int:
    lowercase_index = string.ascii_lowercase.index(item.lower())
    if item.isupper():
        return lowercase_index + 27
    return lowercase_index + 1


groups = read_input()
priority_sum = 0
for group in groups:
    badge_item = None
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badge_item = item
            break
    priority_sum += get_priority(badge_item)
print(priority_sum)
