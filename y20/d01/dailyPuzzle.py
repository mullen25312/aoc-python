from utils.superDailyPuzzle import SuperDailyPuzzle

class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self):
        for idx1, num1 in enumerate(self.parsed):
            for idx2, num2 in enumerate(self.parsed):
                if idx1 == idx2:
                    break
                if num1 + num2 == 2020:
                    self.part_one_result = num1 * num2

    def part_two(self):
        for idx1, num1 in enumerate(self.parsed):
            for idx2, num2 in enumerate(self.parsed):
                for idx3, num3 in enumerate(self.parsed):
                    if idx1 == idx2 or idx1 == idx2 or idx1 == idx3:
                        break
                    if num1 + num2 + num3 == 2020:
                        self.part_two_result =  num1 * num2 * num3
