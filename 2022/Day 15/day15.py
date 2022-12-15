from tqdm import tqdm
import re

REGEX = re.compile(r"-?\d+")
LINES = list(open("day15input.txt", "r"))


def get_covered_x_poses(row: int):
    beacon_x_poses = set()  # Set of X coordinates, along the given "row", that contain a beacon
    covered_bounds = []  # List of X coordinate bounds that each sensor covers (can overlap each other).
    for line in LINES:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, REGEX.findall(line))
        distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        distance_to_row = abs(sensor_y - row)
        # Offset of the bottom of the boundary from the row:
        # eg: if boundary_offset = 1, the Y pos of the bottom of the boundary is 1 higher than the row
        boundary_offset = distance_to_beacon - distance_to_row
        # If boundary_offset is negative, the boundary never touches the row, thus the sensor never covers the row
        if boundary_offset < 0:
            continue
        # Add beacon X pos to set, if beacon lies on the row
        if beacon_y == row:
            beacon_x_poses.add(beacon_x)
        # The edge of the boundary to the left and right will be the same distance as the boundary_offset
        start_x = sensor_x - boundary_offset
        end_x = sensor_x + boundary_offset
        covered_bounds.append([start_x, end_x])

    covered_bounds.sort()  # Sort bounds from lowest to highest start X, then lowest to highest end X

    # Create new list of bounds that DO NOT OVERLAP each other
    covered_bounds_no_overlap = []
    for start_x, end_x in covered_bounds:
        if not covered_bounds_no_overlap:
            covered_bounds_no_overlap.append([start_x, end_x])
            continue
        last_start_x, last_end_x = covered_bounds_no_overlap[-1]
        # If the start X of the current bound is higher than the end X of the last bound,
        # then they are not overlapping.
        # If the start X of the current bound is ALSO higher than ONE MORE THAN the end X of the last bound,
        # then the two bounds are also not TOUCHING.
        if start_x > last_end_x + 1:
            # Bound is not overlapping or touching with the last bound, so it has to be added as a new bound
            covered_bounds_no_overlap.append([start_x, end_x])
            continue
        # Otherwise, the current bound is either overlapping or touching the last bound, so they should be merged.
        # The start X of the merged bound will be the last starting X, because the bounds were sorted.
        # The end X of the merged bound will be the highest of the two bound's
        covered_bounds_no_overlap[-1][1] = max(last_end_x, end_x)  # Update end X

    # Now we can iterate over each bound without re-counting because they no longer overlap
    covered_x_poses = set()  # Set of X coordinates, along the given "row", that are covered by at least 1 sensor
    for start_x, end_x in covered_bounds_no_overlap:
        for x in range(start_x, end_x + 1):
            covered_x_poses.add(x)

    return len(covered_x_poses) - len(beacon_x_poses)


def get_tuning_frequency(max_xy: int):
    for row in tqdm(range(max_xy + 1)):
        covered_bounds = []  # List of X coordinate bounds that each sensor covers (can overlap each other).
        for line in LINES:
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, REGEX.findall(line))
            distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            distance_to_row = abs(sensor_y - row)
            # Offset of the bottom of the boundary from the row:
            # eg: if boundary_offset = 1, the Y pos of the bottom of the boundary is 1 higher than the row
            boundary_offset = distance_to_beacon - distance_to_row
            # If boundary_offset is negative, the boundary never touches the row, thus the sensor never covers the row
            if boundary_offset < 0:
                continue
            # The edge of the boundary to the left and right will be the same distance as the boundary_offset
            start_x = sensor_x - boundary_offset
            end_x = sensor_x + boundary_offset
            covered_bounds.append([start_x, end_x])

        covered_bounds.sort()  # Sort bounds from lowest to highest start X, then lowest to highest end X

        # Create new list of bounds that DO NOT OVERLAP each other
        covered_bounds_no_overlap = []
        for start_x, end_x in covered_bounds:
            if not covered_bounds_no_overlap:
                covered_bounds_no_overlap.append([start_x, end_x])
                continue
            last_start_x, last_end_x = covered_bounds_no_overlap[-1]
            # If the start X of the current bound is higher than the end X of the last bound,
            # then they are not overlapping.
            # If the start X of the current bound is ALSO higher than ONE MORE THAN the end X of the last bound,
            # then the two bounds are also not TOUCHING.
            if start_x > last_end_x + 1:
                # Bound is not overlapping or touching with the last bound, so it has to be added as a new bound
                covered_bounds_no_overlap.append([start_x, end_x])
                continue
            # Otherwise, the current bound is either overlapping or touching the last bound, so they should be merged.
            # The start X of the merged bound will be the last starting X, because the bounds were sorted.
            # The end X of the merged bound will be the highest of the two bound's
            covered_bounds_no_overlap[-1][1] = max(last_end_x, end_x)  # Update end X

        x = 0
        for start_x, end_x in covered_bounds_no_overlap:
            if x < start_x:  # X is outside the current bound
                return (x * 4000000) + row  # Return tuning frequency
            else:  # X is inside the current bound, so skip to the end
                x = end_x + 1
            if x > max_xy:  # If skipping outside the bound causes X to go beyond the limit, break out the loop
                break


# Part 1
print(get_covered_x_poses(2000000))
# Part 2
print(get_tuning_frequency(4000000))
