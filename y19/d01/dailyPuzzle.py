from utils.superDailyPuzzle import SuperDailyPuzzle
import math

# advent of code 2019 day 1
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self):
        self.part_one_result = sum([max((math.floor(value / 3) - 2, 0)) for value in self.parsed])

    def part_two(self):
        data = [max((math.floor(value / 3) - 2, 0)) for value in self.parsed]
        result = data
        while any(value != 0 for value in data):
            data = [max((math.floor(value / 3) - 2, 0)) for value in data]
            result = result + data
        self.part_two_result = sum(result)