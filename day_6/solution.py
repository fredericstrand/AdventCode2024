class Grid:
    def __init__(self, input_file):
        with open(input_file, "r") as data:
            lines = data.read().strip().split("\n")

        self.grid = lines
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.obstacles = set()
        self.guard = None

        self.parse_grid()

    def parse_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if cell in "^<>v":
                    self.guard = Guard((row, col), cell, self)
                elif cell == "#":
                    self.obstacles.add((row, col))

    def is_valid_position(self, position):
        row, col = position
        return (0 <= row < self.rows) and (0 <= col < self.cols) and position not in self.obstacles


    def is_out_of_bounds(self, position):
        row, col = position
        return not (0 <= row < self.rows and 0 <= col < self.cols)


class Guard:
    DIRECTIONS = {'^': (1, 0), '>': (0, 1), 'v': (-1, 0), '<': (0, -1)}
    TURN_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    def __init__(self, start_position, direction, grid):
        self.position = start_position
        self.direction = direction
        self.grid = grid
        self.visited_positions = set()
        self.visited_positions.add(self.position)


    def move(self):
        dir_row, dir_col = self.DIRECTIONS[self.direction]
        next_position = (self.position[0] + dir_row, self.position[1] + dir_col)

        if self.grid.is_valid_position(next_position):
            self.position = next_position
            self.visited_positions.add(self.position)
        else:
            self.turn_right()


    def turn_right(self):
        self.direction = self.TURN_RIGHT[self.direction]

    def patrol(self):
        last_position = None
        last_direction = None

        while not self.grid.is_out_of_bounds(self.position):
            self.move()

        return len(self.visited_positions)


grid = Grid("input.txt")
result = grid.guard.patrol()
print(f"Distinct positions: {result}")
