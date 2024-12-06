import re

def read_puzzle(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == "__main__":
    line = read_puzzle("puzzle_3.txt")
    complete_line = "".join(line)
    
    x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", complete_line)
    print(x)
    multiplied_number_result = 0
    
    should_multiply = True
    
    for i in x:
        if i == "don't()":
            should_multiply = False
        elif i == "do()":
            should_multiply = True
        if should_multiply:
         # Now I will just find the numbers, now that I know this is valid
            valid_numbers = re.findall(r"\d+,\d+", i)
            for valid_number in valid_numbers:
                numbers = valid_number.split(",")
                print(numbers)
                if len(numbers[0]) > 3 or len(numbers[1]) > 3:
                    continue
                multiplied_number_result += int(numbers[0]) * int(numbers[1])
    
    print(multiplied_number_result)