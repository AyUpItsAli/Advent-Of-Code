buffer = open("day6input.txt", "r").readline().strip("\n")


def num_chars_before_marker(marker_length: int):
    for i in range(len(buffer)):
        chars = buffer[i:i+marker_length]
        if len(list(chars)) == len(set(chars)):
            return i + marker_length


# Part 1
print(num_chars_before_marker(4))
# Part 2
print(num_chars_before_marker(14))
