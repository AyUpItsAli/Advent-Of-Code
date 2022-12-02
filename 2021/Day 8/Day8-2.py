def read_input(path):
    entries = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            entry = []
            for n in line.strip("\n").split(" | "):
                entry.append(n.split(" "))
            entries.append(entry)
            line = file.readline()

    return entries

entries = read_input("day 8.txt")

total = 0
for entry in entries:
    
    # Define the digits that we know
    # 1, 4, 7 and 8 are simple to find
    digits = {}
    for signal in entry[0]:
        if len(signal) == 2: digits[1] = signal
        elif len(signal) == 4: digits[4] = signal
        elif len(signal) == 3: digits[7] = signal
        elif len(signal) == 7: digits[8] = signal

    # The digits with 6 segments are 0, 6, and 9
    # We can identify them with the following statements:

    # 6 Doesn't have ALL of 4 and 1's segments
    # 9 has ALL of 4 and ALL of 1's segments
    # 0 Doesn't have ALL of 4's segments, but does have ALL of 1's segments

    # Implement the above statements into if statements:
    for signal in entry[0]:
        if len(signal) == 6:

            # Does the signal contain segments in 4
            has_four = True
            for char in digits[4]:
                if char not in signal:
                    has_four = False

            # Does the signal contain segments in 1
            has_one = True
            for char in digits[1]:
                if char not in signal:
                    has_one = False
            
            if has_four and has_one:
                digits[9] = signal
            elif not has_four and not has_one:
                digits[6] = signal
            elif not has_four and has_one:
                digits[0] = signal

    # Next are the digits with 5 segments,
    # which are 2, 3, and 5
    # We can identify them with the following statements:

    # 3 has ALL of 1's segments (2 and 5 don't)
    # 5 doesn't have ALL of 1's segments and has one segment that isn't in 6
    # 2 doesn't follow the statements above (so, the "else" block)

    # Implement the above statements into if statements:
    for signal in entry[0]:
        if len(signal) == 5:

            # Does the signal contain segments in 1
            has_one = True
            for char in digits[1]:
                if char not in signal:
                    has_one = False

            if has_one: digits[3] = signal
            else:

                # How many segments are not in 6?
                num_not_in_6 = 0
                for char in digits[6]:
                    if char not in signal:
                        num_not_in_6 += 1

                if num_not_in_6 == 1: digits[5] = signal
                else: digits[2] = signal

    # For every digit after the "|" sign, find which digit it matches
    entry_total = ""
    for digit in entry[1]:
        for d in digits:
            if len(digit) == len(digits[d]):
                same_digit = True
                for char in digit:
                    if char not in digits[d]:
                        same_digit = False
                if same_digit:
                    # Then concatenate that digit, as a string, to entry_total
                    entry_total += str(d)
    
    # Finally convert entry_total into a 4 digit integer
    total += int(entry_total)

print(total)