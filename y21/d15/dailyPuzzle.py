from utils.superDailyPuzzle import SuperDailyPuzzle

from dijkstra import DijkstraSPF
import copy

class myDijkstraSPF(DijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        x, y = u
        (n, m) = (len(G), len(G[0]))

        tmp = []
        for (dx, dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5*m and 0 <= ny < 5*n:
                tmp.append((nx, ny))
        return tmp

    @staticmethod
    def get_edge_weight(G, u, v):
        grid = G
        (n, m) = (len(grid), len(grid[0]))
        x = v[0] % m
        y = v[1] % n
        return ((grid[y][x] + v[0] // m + v[1] // n) - 1) % 9 + 1

class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = []
        for line in self.data.splitlines():
            self.parsed.append([int(x) for x in list(line)])

    def part_one(self):
        grid = copy.deepcopy(self.parsed)

        # avoid shortcuts due to part two extension
        for line in grid: line.append(9)
        grid.append([9]*len(grid[0]))

        (n, m) = (len(grid), len(grid[0]))
        S = ((0,0))
        E = (m-2, n-2)

        dijkstra = myDijkstraSPF(grid, S)
        self.part_one_result = dijkstra.get_distance(E)

    def part_two(self):
        grid = copy.deepcopy(self.parsed)
        (n, m) = (len(grid), len(grid[0]))
        S = ((0,0))
        E = (5*m-1, 5*n-1)

        dijkstra = myDijkstraSPF(grid, S)
        self.part_two_result = dijkstra.get_distance(E)