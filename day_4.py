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

# def check_straight_direction(index_direction: tuple[int, int], index, lines, is_left_right: bool):
#     test_string = ""

#     for i in range(4):
#         if is_left_right:
#             if i + index[1]


# This function will take an index and find all the possible directions and return the number
# of times xmas appeared for that individual location
def find_xmas(index: tuple[int, int], lines: list[list]):
    matches = 0


    # Check up
    up_string = ""
    for y in range(4):
        if y - index[1] < 0:
            break
        else:
            up_string += lines[index[0], y - index[1]]

    if up_string == "XMAS":
        matches += 1 


    # Check Down
    down_string = ""
    for y in range(4):
        if y + index[1] >= lines.shape[1]:
            break
        else:
            down_string += lines[index[0], y + index[1]]

    if down_string == "XMAS":
        matches += 1 


    # Check Left
    left_string = ""
    for x in range(4):
        if x - index[0] < 0:
            break
        else:
            left_string += lines[x - index[0], index[1]]
    if left_string == "XMAS":
        matches += 1 

    # Check Right
    right_string = ""
    for x in range(4):
        if x - index[0] >= lines.shape[0]:
            break
        else:
            right_string += lines[x - index[0], index[1]]
    if right_string == "XMAS":
        matches += 1 

    # Check Up Left Diagonal


    # Check Up Right Diagonal

    # Check Down Left Diagonal

    # Check Down Right Diagonal

    # print(matches)

    return matches




if __name__ == "__main__":
    lines = read_file("examples/example_4.txt")

    matches = 0
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            matches += find_xmas((i, j), lines)

    print(f"Total Matches: {matches}")
