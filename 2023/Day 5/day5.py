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
    sorted_results = sorted(results)
    print(sorted_results[0])


part_1("input.txt")
