from utils.superDailyPuzzle import SuperDailyPuzzle
from utils.tree import Tree

# advent of code 2022 day 06
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = self.data

        # store universal orbital map as tree in data
        self.parsed = Tree()
        self.parsed.add_child("COM")
        # self.parsed.print_tree()

    def part_one(self):
        self.part_one_result = 0

    def part_two(self):
        self.part_two_result = 0
