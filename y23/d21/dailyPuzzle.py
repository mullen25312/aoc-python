from utils.superDailyPuzzle import SuperDailyPuzzle

neighbors = [(-1,0), (1,0), (0,-1), (0,1)]

# advent of code 2023 day 21
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        grid = []
        start = (0,0)
        for idx, line in enumerate(self.data.splitlines()):
            grid.append([0 if (x=="." or x=="S") else 1 for x in list(line)])
            if "S" in line: start = (idx, list(line).index("S"))

        self.parsed = (grid, start)

    def part_one(self):
        (grid, start) = self.parsed
        (n, m) = (len(grid), len(grid[0]))

        reachables = [{start}]
        for idx in range(0, 64):
            reachable = set()
            for pos in reachables[-1]:
                for neighbor in neighbors:
                    tmp = (pos[0]+neighbor[0], pos[1]+neighbor[1])
                    if (0 <= tmp[0] < n) and (0 <= tmp[1] < m) and (grid[tmp[0]][tmp[1]] == 0):
                        reachable.add((pos[0]+neighbor[0], pos[1]+neighbor[1]))
            reachables.append(reachable)

        self.part_one_result = len(reachables[-1])

    def part_two(self):
        (grid, start) = self.parsed
        (n, m) = (len(grid), len(grid[0]))

        reachables = [{start}]
        for idx in range(0, 500):
            # print(idx)
            reachable = set()
            for pos in reachables[-1]:
                for neighbor in neighbors:
                    tmp = (pos[0]+neighbor[0], pos[1]+neighbor[1])
                    if (grid[tmp[0] % n][tmp[1] % m] == 0):
                        reachable.add((pos[0]+neighbor[0], pos[1]+neighbor[1]))
            reachables.append(reachable)

        self.part_two_result = len(reachables[-1])
