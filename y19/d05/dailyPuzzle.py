from utils.superDailyPuzzle import SuperDailyPuzzle
from utils.intcode_computer import IntcodeComputer

# advent of code 2019 day 5
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = self.data.split(",")
        self.parsed = [int(line) for line in lines]

    def part_one(self):
        program = self.parsed.copy()
        intcode_computer = IntcodeComputer(program, [1])
        intcode_computer.run_until_termination()
        self.part_one_result = intcode_computer.outputs[-1]

    def part_two(self):
        program = self.parsed.copy()
        intcode_computer = IntcodeComputer(program, [5])
        intcode_computer.run_until_termination()
        self.part_two_result = intcode_computer.outputs[-1]