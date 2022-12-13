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


# Part 1
pairs = read_input()
sum_indices = 0
for i, pair in enumerate(pairs):
    if compare_list(pair[0], pair[1]):
        sum_indices += i + 1
print(sum_indices)


def bubble_sort(packets: list):
    while True:
        swapped = False
        for i in range(len(packets[:-1])):
            packet = packets[i]
            next_packet = packets[i + 1]
            if not compare_list(packet, next_packet):
                packets[i] = next_packet
                packets[i + 1] = packet
                swapped = True
        if not swapped:
            break


# Part 2
packets = [packet for pair in pairs for packet in pair]  # Flattens 2D array of pairs into list of packets
packets.extend([  # Add divider packets
    [[2]],
    [[6]]
])
bubble_sort(packets)
decoder_key = 1
for i, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        decoder_key *= i + 1
print(decoder_key)
