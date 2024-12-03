import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total_result = 0
with open("input.txt","r") as data:
    matches = []
    for line in data:
        matches = re.findall(pattern, line)

        total_result += sum(int(i) * int(j) for i,j in matches)


print(total_result)        