from utils.superDailyPuzzle import SuperDailyPuzzle


def sum_of_ints(number):
    return number * (number + 1) // 2


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = [int(number) for number in self.data.splitlines()[0].split(",")]

    def part_one(self):

        min_fuel = sum([abs(crab - self.parsed[0]) for crab in self.parsed])
        for pos in range(min(self.parsed), max(self.parsed)):
            tmp = sum([abs(crab - pos) for crab in self.parsed])
            min_fuel = min(min_fuel, tmp)

        self.part_one_result = min_fuel

    def part_two(self):
        min_fuel = sum([sum_of_ints(abs(crab - self.parsed[0])) for crab in self.parsed])

        # do not check the whole range as the fuel does not increase linearly anymore (half the range seems to be enough)
        mean = (max(self.parsed) - min(self.parsed)) // 2
        for pos in range(mean + (min(self.parsed) - mean) // 2, mean + (max(self.parsed) - mean) // 2):
            tmp = sum([sum_of_ints(abs(crab - pos)) for crab in self.parsed])
            # min_fuel = min(min_fuel, tmp)
            min_fuel = min(min_fuel, tmp)

        self.part_two_result = min_fuel
