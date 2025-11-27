from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2023 day 20
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        modules = {}
        for line in self.data.splitlines():
            start = line.split("->")[0].strip()
            if list(start)[0] == "%" or list(start)[0] == "&":
                type = list(start)[0] 
                start = start[1:]
            else:
                type = None
            ends = [x.strip() for x in line.split("->")[1].strip().split(",")]
            modules[start] = (type, ends)
        self.parsed = modules

    def part_one(self):
        self.part_one_result = 0

    def part_two(self):
        self.part_two_result = 0