import json

ROOT = "/"
file_system = {}


# Returns the directory dict for the given path
def get_directory(directory_path: list) -> dict:
    directory = file_system  # Start at the root
    for sub_directory in directory_path:  # Iterate over sub dirs, down to the last dir in the path
        directory = directory[sub_directory]
    return directory


# Creates a new directory at the given path, then returns the new path to that directory
def create_new_directory(new_directory: str, directory_path: list) -> list:
    parent_directory = get_directory(directory_path)  # Get where this directory will be located
    parent_directory[new_directory] = {}  # Add new empty directory to the parent directory
    directory_path.append(new_directory)  # Update the path
    return directory_path  # Return the new path, which now points inside the newly created directory


# Adds a new file to the directory at the given path
def add_file(file: list, directory_path: list) -> None:
    file_size = int(file[0])  # Gather file data
    file_name = file[1]
    directory = get_directory(directory_path)  # Get the directory at the given path
    directory[file_name] = file_size  # Add the file to the directory


# 1: Traverses the file system via the commands in the puzzle input.
# 2: Builds the file_system dict as it traverses the file system.
def create_file_system() -> None:
    current_path = []  # Path to the current directory we are in. Empty list = at ROOT
    with open("day7input.txt", "r") as file:
        line = file.readline()  # Read the first line
        while line != "":  # Continue loop until the end of the file is reached
            if not line.startswith("$"):
                line = file.readline()  # If this line is not a command, read the next line
            else:
                # If the line is a command, split the command into two parts: the command name and the first parameter
                command = line.strip("\n").strip("$ ").split(" ")
                if command[0] == "cd":
                    new_directory = command[1]  # First parameter is the name of the new directory
                    if new_directory == ".." and current_path:
                        # If ".." was passed, simply remove the last element of the path (going back 1 level)
                        current_path.pop()
                    elif new_directory == ROOT:
                        current_path = []  # If "/" was passed, return to the root
                    else:
                        # Otherwise, create a new directory at the current path,
                        # then set the current path to the path of the new directory
                        current_path = create_new_directory(new_directory, current_path)
                    line = file.readline()  # At the end of the command, read the next line
                elif command[0] == "ls":
                    line = file.readline()  # Read the first line, after the ls command was executed
                    # Continue this loop until we reach a new command or the end of the file
                    while not line.startswith("$") and line != "":
                        if not line.startswith("dir"):  # Ignore directories, as we already added them via the cd command
                            # We now know this is a file, so we split at the space character (" ")
                            # This gives a list where the first element is the file size and the second element is the name
                            child_file = line.strip("\n").split(" ")
                            add_file(child_file, current_path)  # Add the file to the current path
                        line = file.readline()  # Read the next line


create_file_system()  # Create the file system, which is stored in the file_system dict
print(json.dumps(file_system, indent=4))  # Print the file system in a fancy way
print("File system above ^^^")


# Returns the sum of file sizes (direct or indirect) for the given directory
def get_directory_size(directory: dict) -> int:
    size = 0
    for child in directory.values():  # Iterate over VALUES, not KEYS!
        if isinstance(child, int):  # If value is an int, it must be a file size
            size += child  # Increment by this file size
        elif isinstance(child, dict):  # If value is a dict, it must be a subdirectory
            size += get_directory_size(child)  # Increment by the size of this subdirectory (recursion)
    return size


# Returns the sum of directory sizes up to 100,000
def get_total_directory_sizes(directory: dict):
    total = 0
    for child in directory.values():
        # Ignore files. We only care about the directory sizes
        if isinstance(child, dict):  # If value is a dict, it must be a subdirectory
            size = get_directory_size(child)
            if size <= 100_000:
                total += size  # If size is at most 100,000 increment total by this size
            # Now repeat the above for the subdirectories of this subdirectory, then add it to the total
            total += get_total_directory_sizes(child)
    return total


# Part 1
print("Part 1: {}".format(get_total_directory_sizes(file_system)))

# Part 2
DISK_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000

used_space = get_directory_size(file_system)
free_space = DISK_SPACE - used_space


# Returns a list of directory sizes that, when deleted, would free up enough space to run the update
def get_sufficient_directory_sizes(directory: dict):
    sufficient_sizes = []
    for child in directory.values():
        # Ignore files. We only care about the directory sizes
        if isinstance(child, dict):  # If value is a dict, it must be a subdirectory
            size = get_directory_size(child)
            if size + free_space >= REQUIRED_SPACE:
                sufficient_sizes.append(size)  # If directory size can free up enough space, add the size to the list
            # Check if there are any subdirectories of this subdirectory that are of sufficient size,
            # and add them to the list using extend()
            sufficient_sizes.extend(get_sufficient_directory_sizes(child))
    return sufficient_sizes


# Begin with the size of the whole file system added to the list, in case we have to remove everything to run the update
sufficient_sizes = [used_space]
sufficient_sizes.extend(get_sufficient_directory_sizes(file_system))  # Add any other sufficient sizes, using extend()
sufficient_sizes.sort()  # Sort the sizes (smallest to biggest)
print("Part 2: {}".format(sufficient_sizes[0]))  # Print the smallest size
