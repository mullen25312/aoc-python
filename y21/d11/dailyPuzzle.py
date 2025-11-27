from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def flash(flasher, octopuses):
    for neighbor in neighbors:
        if (0 <= flasher[0] + neighbor[0] <= octopuses.shape[0] - 1) and (0 <= flasher[1] + neighbor[1] <= octopuses.shape[1] - 1):
            if octopuses[flasher[0] + neighbor[0], flasher[1] + neighbor[1]] != 0:
                octopuses[flasher[0] + neighbor[0], flasher[1] + neighbor[1]] += 1
    return octopuses


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = np.array([[int(digit) for digit in list(line)] for line in self.data.splitlines()])

    def part_one(self):
        octopuses = np.copy(self.parsed)
        number_of_steps = 100
        flashes = 0

        for idx in range(number_of_steps):
            flashed = set()
            octopuses = octopuses + 1

            while np.any((octopuses > 9)):
                flasher = np.argwhere(octopuses > 9)[0]
                octopuses = flash(flasher, octopuses)
                flashes += 1
                octopuses[flasher[0], flasher[1]] = 0

        self.part_one_result = flashes

    def part_two(self):
        octopuses = np.copy(self.parsed)
        flashes = 0
        steps = 0

        while not np.all(octopuses == 0):
            flashed = set()
            octopuses = octopuses + 1

            while np.any((octopuses > 9)):
                flasher = np.argwhere(octopuses > 9)[0]
                octopuses = flash(flasher, octopuses)
                octopuses[flasher[0], flasher[1]] = 0
            steps += 1

        self.part_two_result = steps
