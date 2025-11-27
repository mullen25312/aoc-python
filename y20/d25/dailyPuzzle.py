from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 25
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self):
        subject_number = 7
        mod_base = 20201227

        tmp = 1
        idx0 = 0
        while tmp != self.parsed[0]:
            tmp = (tmp*subject_number) % mod_base
            idx0 += 1

        tmp = 1
        idx1 = 0
        while tmp != self.parsed[1]:
            tmp = (tmp*subject_number) % mod_base
            idx1 += 1 

        key = 1
        for _ in range(idx0):
            key = (key*self.parsed[1]) % mod_base

        self.part_one_result = key
        
    def part_two(self):
        self.part_two_result = 0