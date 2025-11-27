from utils.superDailyPuzzle import SuperDailyPuzzle
from collections import defaultdict

def neighbors(cube1, cube2):
    if cube1 == cube2:
        return False
    elif cube1[0] == cube2[0] and cube1[1] == cube2[1] and (cube1[2] == cube2[2] + 1 or cube1[2] == cube2[2] - 1) or \
            cube1[0] == cube2[0] and cube1[2] == cube2[2] and (cube1[1] == cube2[1] + 1 or cube1[1] == cube2[1] - 1) or \
            cube1[2] == cube2[2] and cube1[1] == cube2[1] and (cube1[0] == cube2[0] + 1 or cube1[0] == cube2[0] - 1):
        return True

# advent of code 2022 day 18
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]

        self.parsed = []
        for line in lines:
            self.parsed.append(tuple(int(x) for x in line.split(",")))

    def part_one(self):
        result1 = defaultdict(lambda: 0)

        for cube1 in self.parsed:
            for cube2 in self.parsed:
                if neighbors(cube1, cube2): result1[cube1] += 1

        self.part_one_result = len(self.parsed)*6-sum(result1.values())

    def part_two(self):
        self.part_two_result = 0
