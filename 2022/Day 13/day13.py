def read_input():
    out = []
    with open("day13input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                packet1 = eval(line.strip("\n"))
                packet2 = eval(file.readline().strip("\n"))
                out.append([packet1, packet2])
            line = file.readline()
    return out


def to_list(value):
    if isinstance(value, list):
        return value
    return [value]


def compare_list(listLeft: list, listRight: list):
    for valueLeft, valueRight in zip(listLeft, listRight):
        if isinstance(valueLeft, list):
            result = compare_list(valueLeft, to_list(valueRight))
            if result is None:
                continue
            return result
        elif isinstance(valueRight, list):
            result = compare_list(to_list(valueLeft), valueRight)
            if result is None:
                continue
            return result
        elif valueLeft == valueRight:
            continue
        return valueLeft < valueRight
    if len(listLeft) == len(listRight):
        return None
    return len(listLeft) < len(listRight)


pairs = read_input()
sum_indicies = 0
for i, pair in enumerate(pairs):
    if compare_list(pair[0], pair[1]):
        sum_indicies += i + 1
print(sum_indicies)
