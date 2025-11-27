from utils.superDailyPuzzle import SuperDailyPuzzle

from dijkstra import DijkstraSPF

class myDijkstraSPF(DijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        x, y = u
        (n, m) = (len(grid), len(grid[0]))

        tmp = []
        for (dx, dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if grid[ny][nx] - grid[y][x] >= -1:
                    tmp.append((nx, ny))
        return tmp

    @staticmethod
    def get_edge_weight(G, u, v):
        return 1
    
# advent of code 2022 day 12
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        grid = []
        for line in self.data.splitlines():
            grid.append([ord(x) for x in list(line)])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ord("S"):
                    start = (col, row)
                    grid[row][col] = ord("a")
                if grid[row][col] == ord("E"):
                    end = (col, row)
                    grid[row][col] = ord("z")

        self.parsed = [grid, start, end]

    def part_one(self):
        grid, start, end = self.parsed

        dijkstra = myDijkstraSPF(grid, end)
        self.part_one_result = dijkstra.get_distance(start)

    def part_two(self):
        grid, start, end = self.parsed
        dijkstra = myDijkstraSPF(grid, end)

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ord("a"):
                    dist = dijkstra.get_distance((col, row))
                    if result == 0 or dist < result: result = dist
        self.part_two_result = result