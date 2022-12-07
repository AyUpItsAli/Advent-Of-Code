import json

ROOT = "/"
file_system = {}


# Creates a new directory at the given path, then returns the new path to that directory
def create_directory(new_directory: str, path: list) -> list:
    pointer = file_system
    for directory in path:
        pointer = pointer[directory]
    pointer[new_directory] = {}
    path.append(new_directory)
    return path


# Adds a new file inside the directory at the given path
def add_file(file: list, directory_path: list) -> None:
    pointer = file_system
    for directory in directory_path:
        pointer = pointer[directory]
    pointer[file[1]] = int(file[0])


# Traverses the file system via the commands in the puzzle input, and builds the file_system dictionary as it does so
def create_file_system() -> None:
    current_path = []
    with open("day7input.txt", "r") as file:
        line = file.readline()
        while line != "":
            if line.startswith("$"):
                command = line.strip("\n").strip("$ ").split(" ")
                if command[0] == "cd":
                    directory = command[1]
                    if directory == ".." and current_path:
                        current_path.pop()
                    elif directory == ROOT:
                        current_path = []
                    else:
                        current_path = create_directory(directory, current_path)
                    line = file.readline()
                elif command[0] == "ls":
                    line = file.readline()
                    while not line.startswith("$") and line != "":
                        if not line.startswith("dir"):
                            child_file = line.strip("\n").split(" ")
                            add_file(child_file, current_path)
                        line = file.readline()
            else:
                line = file.readline()


create_file_system()
print(json.dumps(file_system, indent=4))


def get_directory_size(directory: dict) -> int:
    size = 0
    for child in directory.values():
        if isinstance(child, int):
            size += child
        elif isinstance(child, dict):
            size += get_directory_size(child)
    return size


def get_total_directory_sizes(directory: dict):
    total = 0
    for child in directory.values():
        if isinstance(child, dict):
            size = get_directory_size(child)
            if size <= 100000:
                total += size
            total += get_total_directory_sizes(child)
    return total


# Part 1
print(get_total_directory_sizes(file_system))
