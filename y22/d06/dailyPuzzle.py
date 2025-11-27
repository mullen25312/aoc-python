from utils.superDailyPuzzle import SuperDailyPuzzle

def find_marker(data, size):
    for idx in range(0, len(data)-(size-1)):
        tmp = ''.join(data[idx:idx+size])
        if len(set(tmp)) == size: return idx+size
    return None

# advent of code 2022 day 06
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        self.parsed = self.data

    def part_one(self):
        self.part_one_result = find_marker(self.parsed, 4)

    def part_two(self):
        self.part_two_result = find_marker(self.parsed, 14)
