from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np


def get_line(point1, point2, mode=0):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    # skip diagonal lines if mode == 1
    if (mode == 1) and not ((x1 == x2) | (y1 == y2)):
        return []

    x = list(range(x1, x2 + (x2 >= x1) - (x2 < x1), np.sign(x2 - x1) + (x1 == x2)))
    y = list(range(y1, y2 + (y2 >= y1) - (y2 < y1), np.sign(y2 - y1) + (y1 == y2)))

    if len(x) == 1:
        x = [x[0] for _ in y]
    if len(y) == 1:
        y = [y[0] for _ in x]

    line = list(zip(x, y))
    return line


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = []
        for line in self.data.splitlines():
            tmp = [tuple(map(int, point.split(","))) for point in line.split(" -> ") if line.strip() != ""]
            self.parsed.append(tmp)

    def part_one(self):
        coord = dict()
        for line in self.parsed:
            for point in get_line(line[0], line[1], mode=1):
                if point in coord.keys():
                    coord[point] += 1
                else:
                    coord[point] = 1

        self.part_one_result = len([point for point in coord if coord[point] >= 2])
        return

    def part_two(self):
        coord = dict()
        for line in self.parsed:
            for point in get_line(line[0], line[1], mode=0):
                if point in coord.keys():
                    coord[point] += 1
                else:
                    coord[point] = 1

        self.part_two_result = len([point for point in coord if coord[point] >= 2])
        return
