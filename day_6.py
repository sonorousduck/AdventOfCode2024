import numpy as np

def read_file(filepath: str) -> tuple[np.ndarray, tuple[int, int]]:
    lines = []
    guard_location = (0, 0) 
    
    with open(filepath) as f:
        for i, line in enumerate(f):
            new_line = []
            for j, ch in enumerate(line.strip()):
                new_line.append(ch)
                
                if ch == "^":
                    guard_location = (j, i)                    
            lines.append(new_line)
    

    return np.array(lines), guard_location

def check_bounds(index: tuple[int, int], lines: np.ndarray) -> bool:
    return index[0] < lines.shape[1] and index[0] >= 0 and index[1] < lines.shape[0] and index[1] >= 0

# Returns a tuple:
# Element 0 indicates guard is out of map
# Element 1 indicates whether the guard was able to move or not
def move_guard(direction: tuple[int, int], guard_location: tuple[int, int], facility_map: np.ndarray, locations_visited: dict) -> tuple[bool, bool]:
    guard_in_map = True
    guard_could_move = True
    
    temp_guard_location = (guard_location[0] + direction[0], guard_location[1] + direction[1])
    
    guard_in_map = check_bounds(temp_guard_location, facility_map)
    
    if guard_in_map:
        if facility_map[temp_guard_location[1], temp_guard_location[0]] == "#":
            guard_could_move = False
        else:
            if temp_guard_location not in locations_visited:
                locations_visited[temp_guard_location] = True
            guard_location = temp_guard_location
    
    
    return (guard_in_map, guard_could_move, guard_location)

def turn_90(direction: tuple[int, int]) -> tuple[int, int]:
    if direction == (0, 1):
        return (-1, 0)
    elif direction == (-1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, 1)
    else:
        return (1, 0)


def run_simulation(guard_location: tuple[int, int], facility_map: np.ndarray) -> int:
    locations_visited = {guard_location: True}
    guard_direction = (0, -1)
    guard_in_map = True
    
    while (guard_in_map):
        guard_in_map, guard_could_move, guard_location = move_guard(guard_direction, guard_location, facility_map, locations_visited)
        if not guard_could_move:
            guard_direction = turn_90(guard_direction)
    
    
    return len(locations_visited.keys())
    
    


if __name__ == "__main__":
    # facility_map, guard_location = read_file("examples/example_6.txt")
    facility_map, guard_location = read_file("puzzles/puzzle_6.txt")
    
    print(run_simulation(guard_location, facility_map))
    
    
    
    
    