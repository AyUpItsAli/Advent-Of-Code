def read_input(path: str):
    cards = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            line = line.strip().replace("  ", " ")
            card = [list(map(int, lst.split(" "))) for lst in line[line.find(":") + 2:].split(" | ")]
            card.append(1)  # Card count
            cards.append(card)
            line = file.readline()
    return cards


def part_1(input_path: str):
    cards = read_input(input_path)
    answer = 0
    for card in cards:
        matches_count = 0
        for num in card[1]:
            if num in card[0]:
                matches_count += 1
        if matches_count > 0:
            answer += 2 ** (matches_count-1)
    print(answer)


def part_2(input_path: str):
    cards = read_input(input_path)
    answer = 0
    for i, card in enumerate(cards):
        matches_count = 0
        for num in card[1]:
            if num in card[0]:
                matches_count += 1
        for j in range(1, matches_count+1):
            cards[i+j][2] += card[2]
    for card in cards:
        answer += card[2]
    print(answer)


part_1("input.txt")
part_2("input.txt")
