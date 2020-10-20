from random import randint

class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.maze = []

    def load_matrix_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.cols, self.rows = map(int, file.readline().split(' '))
            for i in range(self.cols):
                row = []
                for j in file.readline().split(' '):
                    row.append(int(j))
                self.maze.append(row)



    def generate_random_maze(self, cols, rows):
        self.maze = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(randint(0, 1))
            self.maze.append(row)

    def print(self):
        for i in range(self.cols):
            for j in range(self.rows):
                print(self.maze[i][j], end=' ')
            print()
