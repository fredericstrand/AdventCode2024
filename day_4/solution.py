import re

with open("input.txt", "r") as data:
    xmas_input = data.read()

def part1(xmas_input):
    lines = xmas_input.split("\n")
    num_xmas = 0
    pattern = r"XMAS"

    # Check horizontal
    for line in lines:
        num_xmas += len(re.findall(pattern, line))
        num_xmas += len(re.findall(pattern[::-1], line))

    # Check vertical
    cols = max(len(line) for line in lines)
    for col in range(cols):
        vertical_line = "".join(row[col] for row in lines if col < len(row))
        num_xmas += len(re.findall(pattern, vertical_line))
        num_xmas += len(re.findall(pattern[::-1], vertical_line))

    # Check diagonals
    rows = len(lines)

    # Top-left to bottom-right and bottom-right to top-left
    for d in range(-(rows - 1), cols):
        diagonal = "".join(lines[i][i - d] for i in range(rows) if 0 <= i - d < len(lines[i]))
        num_xmas += len(re.findall(pattern, diagonal))
        num_xmas += len(re.findall(pattern[::-1], diagonal))

    # Top-right to bottom-left and bottom-left to top-right
    for d in range(rows + cols - 1):
        diagonal = "".join(lines[i][d - i] for i in range(rows) if 0 <= d - i < len(lines[i]))
        num_xmas += len(re.findall(pattern, diagonal))
        num_xmas += len(re.findall(pattern[::-1], diagonal))

    return num_xmas

print(part1(xmas_input))
