from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

def check_symmetry(pattern, index):
    width = min(pattern.shape[0]-(index+1), index+1)
    return np.all(pattern[index+1:index+width+1] == np.flipud(pattern[index-width+1:index+1]))

def find_mirror(pattern):
    for idx, row in enumerate(pattern[:-1]):
        if check_symmetry(pattern, idx): 
            return idx+1
    return 0

    
# advent of code 2023 day 13
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp = self.data.splitlines()

        patterns = []
        pattern = []
        for line in tmp:
            if line == "":
                patterns.append(np.array(pattern,  dtype=np.uint8))
                pattern = []
            else:
                pattern.append([1 if x == "#" else 0 for x in line])
        patterns.append(np.array(pattern,  dtype=np.uint8))

        self.parsed = patterns

    def part_one(self):
        patterns = self.parsed

        rows, cols = [], []
        for pattern in patterns:
            rows.append(find_mirror(pattern))
            cols.append(find_mirror(np.transpose(pattern)))

        self.part_one_result = sum(rows) * 100 + sum(cols)

    def part_two(self):
        self.part_two_result = 0