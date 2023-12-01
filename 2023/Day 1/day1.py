def read_input(path: str):
    out = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            out.append(line.strip("\n"))
            line = file.readline()
    return out


def part_1(input_path: str):
    lines = read_input(input_path)
    total = 0
    for line in lines:
        digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
        total += int(digits[0] + digits[-1])
    print(total)


def part_2(input_path: str):
    lines = read_input(input_path)
    total = 0
    for line in lines:
        digits = []
        for i,char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            for j,word in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(word):
                    digits.append(str(j+1))
        total += int(digits[0] + digits[-1])
    print(total)


part_1("input.txt")  # 55816
part_2("input.txt")  # 54980
