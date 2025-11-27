from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 19
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.rules = {}
        self.parsed = []
        
        rules_finished = False
        for line in self.data.split('\n'):
            if rules_finished == False:
                if line == '':
                    rules_finished = True
                else:
                    num = int(line.split(':')[0].strip())
                    rule = line.split(':')[1].strip()
                    self.rules[num] = rule
            else:
                if line.strip():  # Only add non-empty lines
                    self.parsed.append(line.strip())

    def part_one(self):
        self.part_one_result = 0
        
    def part_two(self):
        self.part_two_result = 0