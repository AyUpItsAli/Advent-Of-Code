def read_input(path: str):
    schematic = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            schematic.append(list(line.strip()))
            line = file.readline()
    return schematic


def part_1(input_path: str):
    schematic = read_input(input_path)
    answer = 0

    def check_char() -> bool:  # Checks if current char has neighbouring symbol
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    neighbour_r = r+i
                    if neighbour_r < 0 or neighbour_r >= len(schematic):
                        continue
                    neighbour_c = c+j
                    if neighbour_c < 0 or neighbour_c >= len(schematic[0]):
                        continue
                    neighbour_char = schematic[neighbour_r][neighbour_c]
                    if neighbour_char != "." and not neighbour_char.isdigit():
                        return True
        return False

    for r in range(len(schematic)):
        num = ""
        num_valid = False
        for c in range(len(schematic[r])):
            char = schematic[r][c]
            if char.isdigit():
                num += char
                if not num_valid:
                    num_valid = check_char()
            else:
                if num_valid:
                    answer += int(num)
                num = ""
                num_valid = False
        if num_valid:
            answer += int(num)

    print(answer)


def part_2(input_path: str):
    schematic = read_input(input_path)
    gears = {}
    answer = 0

    for r in range(len(schematic)):
        num = ""
        gear_positions = []
        for c in range(len(schematic[r])+1):
            if c < len(schematic[r]) and schematic[r][c].isdigit():
                num += schematic[r][c]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i == 0 and j == 0):
                            neighbour_r = r + i
                            if neighbour_r < 0 or neighbour_r >= len(schematic):
                                continue
                            neighbour_c = c + j
                            if neighbour_c < 0 or neighbour_c >= len(schematic[0]):
                                continue
                            neighbour_char = schematic[neighbour_r][neighbour_c]
                            if neighbour_char == "*":
                                pos = (neighbour_r, neighbour_c)
                                if pos not in gear_positions:
                                    gear_positions.append(pos)
            elif num.isdigit():
                for gear_pos in gear_positions:
                    if gear_pos in gears:
                        gears[gear_pos].append(int(num))
                    else:
                        gears[gear_pos] = [int(num)]
                num = ""
                gear_positions = []

    for numbers in gears.values():
        if len(numbers) == 2:
            answer += (numbers[0] * numbers[1])

    print(answer)


part_1("input.txt")
part_2("input.txt")
