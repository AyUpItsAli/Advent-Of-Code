def read_input(path: str):
    games = {}
    with open(path, "r") as file:
        line = file.readline()
        while line:
            game = line.strip().replace("Game ", "").split(": ")
            game_id = game[0]
            game_info = game[1]
            cube_sets = []
            for cs in game_info.split("; "):
                cube_set = {}
                for c in cs.split(", "):
                    cube = c.split(" ")
                    cube_set[cube[1]] = int(cube[0])
                cube_sets.append(cube_set)
            games[game_id] = cube_sets
            line = file.readline()
    return games


CUBES = {"red": 12, "green": 13, "blue": 14}


def part_1(input_path: str):
    games = read_input(input_path)
    answer = 0
    for game_id, cube_sets in games.items():
        possible = True
        for cube_set in cube_sets:
            for colour, quantity in cube_set.items():
                if quantity > CUBES[colour]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            answer += int(game_id)
    print(answer)


def part_2(input_path: str):
    games = read_input(input_path)
    answer = 0
    for game_id, cube_sets in games.items():
        min_cubes = {}
        for cube_set in cube_sets:
            for colour, quantity in cube_set.items():
                if colour not in min_cubes or quantity > min_cubes[colour]:
                    min_cubes[colour] = quantity
        power = 1
        for quantity in min_cubes.values():
            power *= quantity
        answer += power
    print(answer)


part_1("input.txt")
part_2("input.txt")
