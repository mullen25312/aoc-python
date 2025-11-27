from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 6
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        groups = []
        group = []
        
        for line in self.data.split('\n'):
            if line == "":
                if group:  # Only append if group is not empty
                    groups.append(group)
                    group = []
            else:
                passenger = set(list(line))
                group.append(passenger)

        if group:  # Don't forget the last group if file doesn't end with newline
            groups.append(group)
            
        self.parsed = groups

    def part_one(self):
        self.part_one_result = sum(map(len, map(lambda group: set.union(*group), self.parsed)))

    def part_two(self):
        self.part_two_result = sum(map(len, map(lambda group: set.intersection(*group), self.parsed)))