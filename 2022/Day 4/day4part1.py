def read_input():
    out = []
    with open("day4input.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                pair = []
                for assignment_string in line.strip("\n").split(","):
                    assignment = [int(x) for x in assignment_string.split("-")]
                    pair.append(assignment)
                out.append(pair)
            line = file.readline()
    return out


def scope_fully_contains_assignment(scope, assignment) -> bool:
    return assignment[0] >= scope[0] and assignment[1] <= scope[1]


pairs = read_input()
pairs_to_reconsider = 0
for pair in pairs:
    a1 = pair[0]
    a2 = pair[1]
    if scope_fully_contains_assignment(a2, a1) or scope_fully_contains_assignment(a1, a2):
        pairs_to_reconsider += 1
print(pairs_to_reconsider)
