from utils.superDailyPuzzle import SuperDailyPuzzle


# advent of code 2020 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(line) for line in self.data.splitlines()]
        self.parsed.sort()
        self.parsed.insert(0, 0)
        self.parsed.append(self.parsed[-1] + 3)

    def part_one(self):
        diffs = [0 for n in range(len(self.parsed) - 1)]
        for idx in range(len(self.parsed) - 1):
            diffs[idx] = self.parsed[idx + 1] - self.parsed[idx]

        one_jolt_diffs = sum(diff == 1 for diff in diffs)
        three_jolt_diffs = sum(diff == 3 for diff in diffs)
        self.part_one_result = one_jolt_diffs * three_jolt_diffs

    def part_two(self):
        diffs = [0 for n in range(len(self.parsed) - 1)]
        for idx in range(len(self.parsed) - 1):
            diffs[idx] = self.parsed[idx + 1] - self.parsed[idx]

        last = -1
        combinations = 1
        for idx, diff in enumerate(diffs):
            if diff == 3:
                if idx != last + 1:
                    num_of_ones = idx - last - 1
                    if num_of_ones <= 3:
                        combinations *= 2 ** (num_of_ones - 1)
                    elif num_of_ones == 4:
                        combinations = combinations * 7
                    else:
                        self.part_two_result = "we got a problem"
                        return
                last = idx
        self.part_two_result = combinations