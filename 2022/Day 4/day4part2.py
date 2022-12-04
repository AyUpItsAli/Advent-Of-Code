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


def assignment_overlaps_scope(assignment, scope) -> bool:
    return (scope[0] <= assignment[0] <= scope[1]) or (scope[1] >= assignment[1] >= scope[0])


pairs = read_input()
pairs_to_reconsider = 0
for pair in pairs:
    a1 = pair[0]
    a2 = pair[1]
    if assignment_overlaps_scope(a1, a2) or assignment_overlaps_scope(a2, a1):
        pairs_to_reconsider += 1
print(pairs_to_reconsider)
