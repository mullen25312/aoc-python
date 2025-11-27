from utils.superDailyPuzzle import SuperDailyPuzzle
import itertools


# advent of code 2020 day 9
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self):
        preamble = 25
        for idx, number in enumerate(self.parsed):
            if idx <= preamble:
                continue
            else:
                sums = [pair[0] + pair[1] for pair in itertools.combinations(self.parsed[idx - preamble : idx], 2)]
                if number not in sums:
                    self.part_one_result = number
                    return

        self.part_one_result = "all are valid"

    def part_two(self):
        sol = 14360655
        for idx in range(len(self.parsed)):
            sequence = []
            idx2 = 0
            while sum(sequence) < sol:
                sequence.append(self.parsed[idx + idx2])
                idx2 += 1
                if sum(sequence) == sol:
                    self.part_two_result = min(sequence) + max(sequence)
                    return

        self.part_two_result = "number not found"