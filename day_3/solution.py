import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

total_result = 0
mul_enabled = True

with open("input.txt", "r") as data:
    for line in data:
        muls = re.split(r"(do\(\)|don't\(\))", line)
        
        for mul in muls:
            mul = mul.strip()
            if re.fullmatch(do_pattern, mul):
                mul_enabled = True
            elif re.fullmatch(dont_pattern, mul):
                mul_enabled = False
            elif mul_enabled:
                matches = re.findall(mul_pattern, mul)
                total_result += sum(int(i) * int(j) for i, j in matches)

print(total_result)
