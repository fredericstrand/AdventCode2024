from collections import defaultdict

with open("input.txt", "r") as data:
    for line in data:
        lines = line.strip().split()
    
    antenna = defaultdict(list)
    width = len(lines[0])
    height = len(lines)

    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            if symbol != ".":
                position = x + y
                antenna[symbol].append(position)

def part1(antenna, width, height):
    antinodes = set()

