class BfsSolver:
    def __init__(self, maze, start_position, finish_position):
        self.mazeInstance = maze
        self.start_position = start_position
        self.finish_position = finish_position
        self.solution = []
        self.solution_found = False
        self.visited = []

    def is_valid_position(self, col, row, cols, rows):
        if 0 <= col < cols and 0 <= row < rows:
            return self.mazeInstance.maze[col][row] == 0

    def solve(self):
        queue = []
        start_col, start_row = self.start_position
        finish_col, finish_row = self.finish_position

        dir_col = (1, -1, 0, 0)
        dir_row = (0, 0, -1, 1)

        queue.append((start_col, start_row))
        self.visited.append((start_col, start_row))

        while len(queue) > 0:
            current_col, current_row = queue.pop(0)

            self.solution.append((current_col, current_row))
            self.mazeInstance.maze[current_col][current_row] = -1

            for dir_c, dir_r in zip(dir_col, dir_row):
                good_next_position = self.is_valid_position(current_col + dir_c, current_row + dir_r, self.mazeInstance.cols, self.mazeInstance.rows)
                not_visited_position = (current_col + dir_c, current_row + dir_r) not in self.visited
                if good_next_position and not_visited_position:
                    queue.append((current_col + dir_c, current_row + dir_r))
                    self.visited.append((current_col + dir_c, current_row + dir_r))

                    if current_col + dir_c == finish_col and current_row + dir_r == finish_row:
                        print('Solution found:')
                        self.solution.append((finish_col, finish_row))
                        self.mazeInstance.maze[finish_col][finish_row] = -1
                        for (col, row) in self.solution:
                            print(f'({row}, {col}) ', end=' ')
                        self.solution_found = True
                        print()
                        return
        if not self.solution_found:
            print('No solution found!')
