class BacktrackingSolver:
    def __init__(self, maze, start_position, finish_position):
        self.mazeInstance = maze
        self.start_col, self.start_row = start_position
        self.finish_col, self.finish_row = finish_position
        self.solution = []
        self.visited = []

    def print_matrix(self):
        for col in range(0, self.mazeInstance.cols):
            for row in range(0, self.mazeInstance.rows):
                print(str(self.mazeInstance.maze[col][row]) + " ", end="")
            print(" ")

    def is_valid_position(self, col, row):
        if 0 <= col < self.mazeInstance.cols and (col, row) not in self.visited and 0 <= row < self.mazeInstance.rows and self.mazeInstance.maze[col][row] == 0:
            return True
        return False

    def solve_maze(self):

        if not self.solve_maze_helper(self.start_col, self.start_row, self.solution):
            print('Solution not found')
            return False
        else:
            print('Solution found [Backtracking]:')
            for (col, row) in self.solution:
                print(f'({row}, {col}) ', end=' ')
            return True

    def solve_maze_helper(self, col, row, solution):
        if col == self.finish_col and row == self.finish_row and self.mazeInstance.maze[col][row] == 0:
            solution.append((col, row))
            self.visited.append((col, row))
            return True

        if self.is_valid_position(col, row):
            solution.append((col, row))
            self.visited.append((col, row))

            if self.solve_maze_helper(col + 1, row, solution):
                return True

            if self.solve_maze_helper(col, row - 1, solution):
                return True

            if self.solve_maze_helper(col, row + 1, solution):
                return True

            if self.solve_maze_helper(col - 1, row, solution):
                return True

            return False



