from utils.superDailyPuzzle import SuperDailyPuzzle
import copy


# advent of code 2020 day 11
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        
        for idx, line in enumerate(self.data.splitlines()):
            tmp = []
            for pos in line:
                if pos == ".":
                    tmp.append(-1)
                elif pos == "L":
                    tmp.append(0)
                else:
                    tmp.append(1)

            self.parsed.append(tmp)

    def part_one(self):
        adjacent = [[1, 0], [1, 1], [0, 1], [0, -1], [-1, 0], [1, -1], [-1, 1], [-1, -1]]

        tmp_old = copy.deepcopy(self.parsed)
        tmp_new = copy.deepcopy(self.parsed)

        for round in range(0, 120):

            for i, row in enumerate(tmp_old):
                for j, col in enumerate(row):

                    # count occupied neighbors
                    occupied = 0
                    for adj in adjacent:
                        if i + adj[0] < 0 or i + adj[0] >= len(tmp_old) or j + adj[1] < 0 or j + adj[1] >= len(row):
                            continue
                        if tmp_old[i + adj[0]][j + adj[1]] == 1:
                            occupied += 1

                    if tmp_old[i][j] == 0:
                        if occupied == 0:
                            tmp_new[i][j] = 1

                    elif tmp_old[i][j] == 1:
                        if occupied >= 4:
                            tmp_new[i][j] = 0

            tmp_old = copy.deepcopy(tmp_new)

        self.part_one_result = sum(row.count(1) for row in tmp_new)

    def part_two(self):
        self.part_two_result = ""