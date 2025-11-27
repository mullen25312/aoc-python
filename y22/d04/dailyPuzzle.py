from utils.superDailyPuzzle import SuperDailyPuzzle

def fully_overlaps(r1, r2):
    return True if set(r1) >= set(r2) or set(r2) >= set(r1) else False

def overlaps(r1, r2):
    return True if set(r1).intersection(set(r2)) else False

# advent of code 2022 day 04
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = [line.strip() for line in self.data.splitlines()]

        self.parsed = []
        for line in lines:
            r1 = range(*[int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1])+1])
            r2 = range(*[int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1])+1])
            self.parsed.append([r1, r2])

    def part_one(self):
        self.part_one_result = sum([fully_overlaps(ranges[0], ranges[1]) for ranges in self.parsed])

    def part_two(self):
        self.part_two_result = sum([overlaps(ranges[0], ranges[1]) for ranges in self.parsed])
