import numpy as np

def read_file(filepath: str) -> np.ndarray:
    lines = []

    with open(filepath) as f:
        for line in f:
            new_line = []
            for ch in line.strip():
                new_line.append(ch)
            lines.append(new_line)
    

    return np.array(lines)

def check_bounds(index: tuple[int, int], lines: np.ndarray) -> bool:
    return index[0] < lines.shape[1] and index[0] >= 0 and index[1] < lines.shape[0] and index[1] >= 0


def check_direction(index_direction: tuple[int, int], index: tuple[int, int], lines: np.ndarray) -> int:  
    potential_string = ""
    
    for i in range(4):
        new_index = (index[0] + (i * index_direction[0]), index[1] + (i * index_direction[1]))
        if check_bounds(new_index, lines):
                potential_string += lines[new_index[1], new_index[0]]
        else:
            break
    
    if potential_string == "XMAS":
        return 1
    return 0

def check_for_x_mas(index: tuple[int, int], lines: np.ndarray) -> int:  
    cross_1 = ""
    cross_2 = ""
    
    middle_of_cross = (index[0] + 1, index[1] + 1)
    
    positions_for_cross_1 = [index, middle_of_cross, (index[0] + 2, index[1] + 2)]
    positions_for_cross_2 = [(index[0] + 2, index[1]), middle_of_cross, (index[0], index[1] + 2)]
    
    for i in positions_for_cross_1:
        if not check_bounds(i, lines):
            return 0
        else:
            cross_1 += lines[i[1], i[0]]
    for i in positions_for_cross_2:
        if not check_bounds(i, lines):
            return 0
        else:
            cross_2 += lines[i[1], i[0]]
            
    
    
    
    if (cross_1 == "MAS" or cross_1 == "SAM") and (cross_2 == "MAS" or cross_2 == "SAM"):
        return 1
    return 0
            


# This function will take an index and find all the possible directions and return the number
# of times xmas appeared for that individual location
def find_xmas(index: tuple[int, int], lines: np.ndarray):
    matches = 0

    horizontal_directions = [-1, 0, 1]
    vertical_directions = [-1, 0, 1]
    # horizontal_directions = [1]
    # vertical_directions = [0]
    
    for vertical_direction in vertical_directions:
        for horizontal_direction in horizontal_directions:
            matches += check_direction((horizontal_direction, vertical_direction), index, lines)
    

    return matches




if __name__ == "__main__":
    # lines = read_file("examples/example_4.txt")
    lines = read_file("puzzles/puzzle_4.txt")

    matches = 0
    matches_part_2 = 0
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            matches += find_xmas((j, i), lines)
            matches_part_2 += check_for_x_mas((j, i), lines)

    print(f"Total Matches: {matches}")
    print(f"Total Cross MASes: {matches_part_2}")
    
