import numpy as np
import pandas as pd

def read_text_file(path: str) -> np.array:
    data = []

    with open(path) as f:
        for line in f:
            data.append([int(i) for i in line.strip().split(" ")])

    return data

def check_is_safe(data_row) -> bool:
    is_descending = False
    if data_row[0] == data_row[1]: # Cannot be the same to be safe
        return False    
    elif data_row[0] > data_row[1]:
        is_descending = True

    for i in range(len(data_row) - 1):
        if is_descending:
            if data_row[i] <= data_row[i + 1]: # if it is descending and this is either the same or greater (so not descending, then return false)
                return False
        else:
            if data_row[i] >= data_row[i + 1]: # if it is ascending and this is either the same or less (so not ascending, then return false)
                return False
        
        difference = abs(data_row[i] - data_row[i + 1])
        if difference > 3:
            return False
    
    return True

# Much smarter ways to do this, I am sure. But BRUTE FORCE!!
def check_subset_safe(data_row: list) -> bool:
    for i in range(len(data_row)):
        if check_is_safe(data_row[:i] + data_row[i + 1:]):
            return True


def check_is_safe_part_2(data_row: list) -> bool:
    is_descending = False
    
    
    if data_row[0] == data_row[1]: # Cannot be the same to be safe
        return check_subset_safe(data_row)

    if data_row[0] > data_row[1]:
        is_descending = True

    i = 0
    while i < len(data_row) - 1:
    # for i in range(len(data_row) - 1):
        if is_descending:
            if data_row[i] <= data_row[i + 1]: # if it is descending and this is either the same or greater (so not descending, then return false)
                return check_subset_safe(data_row)


        else:
            if data_row[i] >= data_row[i + 1]: # if it is ascending and this is either the same or less (so not ascending, then return false)
                return check_subset_safe(data_row)

        
        difference = abs(data_row[i] - data_row[i + 1])
        if difference > 3:
            return check_subset_safe(data_row)
        
        i += 1
    
    return True


if __name__ == "__main__":
    data = read_text_file("puzzle_2.txt")
    safe_reports = 0


    for i in data:
        if check_is_safe_part_2(i):
            safe_reports += 1
            print(i)
    
    print(safe_reports)

    