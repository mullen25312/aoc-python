from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find_low_points(heightmap):
    low_points = set()
    for x, y in np.ndindex(heightmap.shape):
        tmp = True
        for neighbor in neighbors:
            if (x + neighbor[0] > heightmap.shape[0] - 1) or (x + neighbor[0] < 0) or (y + neighbor[1] > heightmap.shape[1] - 1) or (y + neighbor[1] < 0):
                continue
            if heightmap[x + neighbor[0], y + neighbor[1]] <= heightmap[x, y]:
                tmp = False
                break
        if tmp:
            low_points.add((x, y))
    return low_points


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = np.array([[int(digit) for digit in list(line)] for line in self.data.splitlines()])

    def part_one(self):
        low_points = find_low_points(self.parsed)
        heights = [self.parsed[low_point] for low_point in low_points]
        self.part_one_result = sum(heights) + len(heights)

    def part_two(self):
        low_points = find_low_points(self.parsed)

        basins = []
        for low_point in low_points:
            basin = set([low_point])

            new_points = set([low_point])
            finished = True
            while finished:
                new_new_points = set()
                for point in new_points:
                    for neighbor in neighbors:
                        if (point[0] + neighbor[0] > self.parsed.shape[0] - 1) or (point[0] + neighbor[0] < 0) or (point[1] + neighbor[1] > self.parsed.shape[1] - 1) or (point[1] + neighbor[1] < 0):
                            continue
                        if (self.parsed[point[0] + neighbor[0], point[1] + neighbor[1]] != 9) and (point[0] + neighbor[0], point[1] + neighbor[1]) not in basin:
                            new_new_points.add((point[0] + neighbor[0], point[1] + neighbor[1]))

                new_points = new_new_points
                basin.update(new_new_points)
                finished = len(new_new_points) != 0
            basins.append(basin)

        basins = sorted(basins, key=lambda x: len(x))

        self.part_two_result = np.prod([len(basin) for basin in basins[-3:]])
