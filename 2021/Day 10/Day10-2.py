def read_input(path):
    lines = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            lines.append(line.strip("\n"))
            line = file.readline()
    
    return lines

lines = read_input("day 10.txt")

opening_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

to_remove = []

for line in lines:
    opened = []

    corrupt_char = None
    for char in line:
        if char in opening_chars:
            opened.append(char)
        else:
            last_opened = opened[len(opened) - 1]
            next_closing = opening_chars[last_opened]
            if char == next_closing:
                opened.pop(len(opened) - 1)
            else:
                corrupt_char = char
                break
    
    if corrupt_char:
        to_remove.append(line)

for line in to_remove:
    lines.remove(line)

scores = []
for line in lines:
    opened = []

    for char in line:
        if char in opening_chars:
            opened.append(char)
        else:
            last_opened = opened[len(opened) - 1]
            next_closing = opening_chars[last_opened]
            if char == next_closing:
                opened.pop(len(opened) - 1)
    
    if opened != []:
        completion_string = ""
        for i in range(len(opened) - 1, -1, -1):
            closing_char = opening_chars[opened[i]]
            completion_string += closing_char

        score = 0
        for char in completion_string:
            score *= 5
            score += points[char]

        scores.append(score)

scores.sort()
middle_index = int((len(scores) - 1) / 2)
print(scores[middle_index])