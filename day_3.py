import re

def read_puzzle(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == "__main__":
    line = read_puzzle("puzzle_3.txt")
    complete_line = "".join(line)
    
    x = re.findall(r"mul\(\d+,\d+\)", complete_line)
    
    multiplied_number_result = 0
    
    for i in x:
         # Now I will just find the numbers, now that I know this is valid
         valid_numbers = re.findall(r"\d+,\d+", i)
         for valid_number in valid_numbers:
            numbers = valid_number.split(",")
            print(numbers)
            if len(numbers[0]) > 3 or len(numbers[1]) > 3:
                continue
            multiplied_number_result += int(numbers[0]) * int(numbers[1])
    
    print(multiplied_number_result)