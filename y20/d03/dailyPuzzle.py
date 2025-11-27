from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 3
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = self.data.splitlines()
        
        tmp = [[""] * len(lines[0]) for i in range(len(lines))]
        for idx1, line in enumerate(lines):
            for idx2, letter in enumerate(line):
                tmp[idx1][idx2] = letter

        self.parsed = tmp

    def part_one(self):
        N = len(self.parsed)
        M = len(self.parsed[0])
        x, y, cnt = 0, 0, 0
        
        while y < N:
            if self.parsed[y][x % M] == "#":
                cnt = cnt + 1
            x = x + 3
            y = y + 1

        self.part_one_result = cnt

    def part_two(self):
        N = len(self.parsed)
        M = len(self.parsed[0])
        slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        prod = 1

        for slope in slopes:
            x, y, cnt = 0, 0, 0
            while y < N:
                if self.parsed[y][x % M] == "#":
                    cnt = cnt + 1
                x = x + slope[0]
                y = y + slope[1]
            prod = prod * cnt

        self.part_two_result = prod