from utils.superDailyPuzzle import SuperDailyPuzzle

def find_duplicate(first, second): # return duplicates of given strings
    return [x for x in first if x in second]

def item_priority(item): # return priority as follows a..z:1..26, A..Z:27..52
    return ord(item) - 38 if item.isupper() else ord(item) - 96

# advent of code 2022 day 03
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [line.strip() for line in self.data.splitlines()]

    def part_one(self):
        duplicates = [find_duplicate(line[:len(line)//2], line[len(line)//2:]) for line in self.parsed]
        self.part_one_result = sum([item_priority(duplicate[0]) for duplicate in duplicates])

    def part_two(self):
        duplicates = [find_duplicate(find_duplicate(x[0], x[1]), x[2]) for x in zip(*[iter(self.parsed)]*3)]
        self.part_two_result =sum([item_priority(duplicate[0]) for duplicate in duplicates])
