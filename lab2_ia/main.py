# from random import randint
#
# """
#     Problema labirintului:
#         Starea problemei va si o lista de coordonate, [(X0, Y0), ... (Xf, Yf)], unde (X0, Y0) este starea initiala, de unde pornim
#         iar (Xf, Yf) este starea finala, unde trebuie sa ajungem (daca este posibil)
#
# """
#
# cols, rows = 100, 100
#
#
# def generateRandomMap(cols, rows):
#     map = []
#     for _ in range(cols):
#         map.append([0] * rows)
#
#     for i in range(cols):
#         for j in range(rows):
#             map[i][j] = randint(0, 1)
#
#     return map
#
#
# def print_map():
#     for i in range(len(map)):
#         for j in range(len(map[0])):
#             print(map[i][j], end=' ')
#         print()
#
#
# def este_stare_finala(x, y, xf, yf):
#     return x == xf and y == yf
#
#
# def initializare(xs, ys, xf, yf):
#     stare.append((xs, ys))
#     visited.append((xs, ys))
#     return xs, ys
#
#
# def coordonata_valida(x, y):
#     if 0 <= x < cols and 0 <= y < rows:
#         return map[x][y] == 0
#     return False
#
#
# def tranzitie_valida(x, y):
#     dir_x = (1, -1, 0, 0)
#     dir_y = (0, 0, 1, -1)
#     for idx, idy in zip(dir_x, dir_y):
#         if coordonata_valida(idx + x, idy + y) and (x, y) not in visited:
#             stare.append((x, y))
#             visited.append((x, y))
#     return stare
#
#
# map = generateRandomMap(cols, rows)
#
# stare = [] # aici vom avea coordonate pe masura ce vizitam
# visited = [] # aici vom avea coordonatele vizitate deja
from Maze import Maze
from BfsSolver import BfsSolver
from BacktrackingSolver import BacktrackingSolver

if __name__ == '__main__':
    maze = Maze(5, 5)
    maze.load_matrix_from_file('matrix_data.txt')

    bfs_solver = BfsSolver(maze, (1, 2), (4, 3))
    bfs_solver.solve()
    maze.print()

    bck_solver = BacktrackingSolver(maze, (1, 2), (4, 3))
    bck_solver.solution()
