from utils.superDailyPuzzle import SuperDailyPuzzle


def sgn(num): return -1 if num < 0 else 1

# advent of code 2025 day 1
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [(((line[0]=='L')*-1 + (line[0]=='R')*1) * int(line[1:])) for line in self.data.splitlines()]

    def part_one(self):
        res = 0; pos = 50
        for step in self.parsed:
            pos = (pos + step) % 100
            res += (pos == 0)
        self.part_one_result = res

    def part_two(self):   
        res = 0; pos = 50
        for step in self.parsed:
            res += abs(step) // 100
            step = sgn(step)* (abs(step) % 100) # for a symmetric modulo
            if not (0 < pos + step < 100) and pos != 0: res += 1
            pos = (pos + step) % 100
        self.part_two_result = res