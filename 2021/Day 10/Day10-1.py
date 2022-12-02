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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
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
        score += points[corrupt_char]

print(score)
        