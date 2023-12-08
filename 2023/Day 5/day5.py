def read_input(path: str):
    with open(path, "r") as file:
        line = file.readline()
        seeds = list(map(int, line.strip().replace("seeds: ", "").split(" ")))
        file.readline()
        line = file.readline()
        maps = []
        while line:
            ranges = []
            while line and line != "\n":
                if not line.strip().endswith(":"):
                    ranges.append(list(map(int, line.strip().split(" "))))
                line = file.readline()
            maps.append(ranges)
            line = file.readline()
    return seeds, maps


def part_1(input_path: str):
    seeds, maps = read_input(input_path)
    results = []
    for seed in seeds:
        result = seed
        for m in maps:
            for r in m:
                if r[1] <= result <= r[1] + r[2] - 1:
                    offset = r[0] - r[1]
                    result += offset
                    break
        results.append(result)
    print(min(results))


def part_2(input_path: str):
    seeds, maps = read_input(input_path)
    input_ranges = [[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0, len(seeds), 2)]

    for m in maps:
        next_input_ranges = []
        while input_ranges:
            input_range = input_ranges.pop()
            i_start = input_range[0]
            i_end = input_range[1]
            for map_range in m:
                m_start = map_range[1]
                m_end = map_range[1] + map_range[2] - 1
                if m_start <= i_end and m_end >= i_start:
                    # Overlap range
                    overlap_range = [max(m_start, i_start), min(m_end, i_end)]
                    o_start = overlap_range[0]
                    o_end = overlap_range[1]

                    # Apply offset to Overlap range
                    offset = map_range[0] - m_start
                    next_input_ranges.append([o_start + offset, o_end + offset])

                    # Feed Underflow and Overflow ranges back in as input ranges
                    if o_start > i_start:
                        input_ranges.append([i_start, o_start-1])
                    if o_end < i_end:
                        input_ranges.append([o_end+1, i_end])
                    break
            else:
                # If no overlaps found, append entire input range
                next_input_ranges.append(input_range)
        input_ranges = next_input_ranges
    print(min(input_ranges)[0])


part_1("input.txt")
part_2("input.txt")
