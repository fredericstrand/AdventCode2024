with open("input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

rules = [tuple(line.split("|")) for line in data[0].splitlines()]
updates = [list(map(int, line.split(","))) for line in data[1].splitlines()]

def is_valid_update(update, rules):
    for x, y in rules:
        x, y = int(x), int(y)
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def get_middle_value(update):
    return update[len(update) // 2] 

total_middle_values = 0
for update in updates:
    if is_valid_update(update, rules):
        total_middle_values += get_middle_value(update)
    

print(total_middle_values)
