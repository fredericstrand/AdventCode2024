from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    return result

def find_valid_expressions(target, numbers):
    for operators in product(['+', '*'], repeat=len(numbers) - 1):
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def solve_puzzle(input_file):
    valid_target_sum = 0
    with open(input_file, "r") as file:
        for line_number, line in enumerate(file, 1):
            if line.strip():
                target, number_sequence = line.strip().split(':')
                target = int(target)
                numbers = list(map(int, number_sequence.strip().split()))
                if find_valid_expressions(target, numbers):
                    valid_target_sum += target
    return valid_target_sum

input_filename = "input.txt"
result = solve_puzzle(input_filename)
print(f"The sum of valid target values is: {result}")
