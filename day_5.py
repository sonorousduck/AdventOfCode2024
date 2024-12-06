
def read_file(filepath: str) -> tuple[dict, list]:
    rules_dictionary = {}
    lines = []

    has_seen_new_line = False
    with open(filepath) as f:
        for line in f:
            if line == "\n":
                has_seen_new_line = True
            else:
                if not has_seen_new_line:
                    rule = line.strip().split('|')

                    if int(rule[0]) not in rules_dictionary:
                        rules_dictionary[int(rule[0])] = []
                    rules_dictionary[int(rule[0])].append(int(rule[1]))

                else:
                    page_order_line = line.strip().split(",")
                    lines.append([int(value) for value in page_order_line])
    return rules_dictionary, lines

def add_up_correct(rules, page_ordering):
    valid_page_lines = []

    for page_line in page_ordering:
        potential_valid_page_line = []
        is_valid = True
        for page in page_line:
            if not is_valid:
                break
            if len(potential_valid_page_line) == 0:
                potential_valid_page_line.append(page)
            else:
                if page in rules:
                    for rule in rules[page]:
                        if rule in potential_valid_page_line:
                            is_valid = False
                            break
                potential_valid_page_line.append(page)
        if is_valid:
            valid_page_lines.append(potential_valid_page_line)
    
    return valid_page_lines


def calculate_invalid_pages_lines(rules, page_ordering):
    invalid_page_lines = []

    for page_line in page_ordering:
        potential_invalid_page_line = []
        is_valid = True
        for page in page_line:
            if not is_valid:
                break
            if len(potential_invalid_page_line) == 0:
                potential_invalid_page_line.append(page)
            else:
                if page in rules:
                    for rule in rules[page]:
                        if rule in potential_invalid_page_line:
                            is_valid = False
                potential_invalid_page_line.append(page)
        if not is_valid:
            invalid_page_lines.append(page_line)
    
    return invalid_page_lines

def reorder_invalid_page_lines(invalid_page_lines, rules):
    reordered_lines = []

    for invalid_page in invalid_page_lines:
        reordered_line = []
        for page in invalid_page:
                # Check the rules. If any of the keys are in the array already, insert before that point
                # If we do this as we go, it will build out the correct order automatically
            best_insert_location = len(reordered_line)
            if page in rules:
                for rule in rules[page]:
                    if rule in reordered_line:
                        insert_location = reordered_line.index(rule)
                        best_insert_location = min(insert_location, best_insert_location)
            reordered_line.insert(best_insert_location, page)
        
        reordered_lines.append(reordered_line)
    
    return reordered_lines

def calculate_middle_sum(page_lines):
    finished_value = 0
    for valid_page_line in page_lines:
        finished_value += valid_page_line[len(valid_page_line) // 2]
    
    print(finished_value)
            

if __name__ == "__main__":
    rules, page_ordering = read_file("puzzles/puzzle_5.txt")
    
    valid_page_lines = add_up_correct(rules, page_ordering)
    calculate_middle_sum(valid_page_lines)

    invalid_page_lines = calculate_invalid_pages_lines(rules, page_ordering)
    reordered_lines = reorder_invalid_page_lines(invalid_page_lines, rules)
    calculate_middle_sum(reordered_lines)

    