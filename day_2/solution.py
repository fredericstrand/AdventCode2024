
# Part 1
def is_safe(level):
    differences = [report1 - report2 for report1, report2 in zip(level, level[1:])]
    is_monotonic = all(i > 0 for i in differences) or all(i < 0 for i in differences)
    good_difference = all(0 < abs(i) <= 3 for i in differences)

    if is_monotonic and good_difference:
        return True

#Part 2
def part2(level):
    if is_safe(level):
        return True
    else:
        # Removing each report to see if the level becomes safe
        for i in range(len(level)):
            modified_level = level[:i] + level[i+1:]
            if is_safe(modified_level):
                return True
    
    return False

with open("input.txt", "r") as data:
    num_safe = 0
    for line in data:
        level = list(map(int, line.strip().split()))
        if part2(level):
            num_safe += 1

print(f"Number of safe levels: {num_safe}")
