from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
from itertools import combinations

def distance(galaxy0, galaxy1):
    return abs(galaxy0[0] - galaxy1[0]) + abs(galaxy0[1] - galaxy1[1])

def grid2list(grid, expand_factor):

    # find rows and cols to be expanded
    rows, cols = [], []
    for idx, row in enumerate(grid):
        if not any(row==1):
            rows.append(idx)
    for idx, col in enumerate(np.transpose(grid)):
        if not any(col==1):
            cols.append(idx)

    # iterate trough grid and collect galaxies
    # and correct their positions according to expansion
    galaxies = []
    for (y,x), _ in np.ndenumerate(grid):
        if grid[y,x] == 1: 
            addy = sum(np.array(rows)<y)*(expand_factor-1)
            addx = sum(np.array(cols)<x)*(expand_factor-1)
            galaxies.append((y+addy,x+addx))
    
    return galaxies
    
# advent of code 2023 day 11
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp = self.data.splitlines()
        n = len(tmp)
        m = len(tmp[0])
        grid = np.zeros((m,n), dtype=np.int8)
        for (y,line) in enumerate(self.data.splitlines()):
            for (x,char) in enumerate(list(line)):
                if char == "#": grid[y,x] = 1
        self.parsed = grid

    def part_one(self):
        self.part_one_result = sum([distance(pair[0], pair[1]) for pair in combinations(grid2list(self.parsed, 2),2)])

    def part_two(self):
        self.part_two_result = sum([distance(pair[0], pair[1]) for pair in combinations(grid2list(self.parsed, 1000000),2)])