from utils.superDailyPuzzle import SuperDailyPuzzle
from utils.intcode_computer import IntcodeComputer

# advent of code 2019 day 2
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp = self.data.strip().split(",")
        self.parsed = [int(i) for i in tmp]

    def part_one(self):
        program = self.parsed.copy()
        program[1] = 12
        program[2] = 2

        intcode_computer = IntcodeComputer(program)
        intcode_computer.run_until_termination()
        self.part_one_result = intcode_computer.program[0]

    def part_two(self):
        for noun in range(100):
            for verb in range(100):
                program = self.parsed.copy()
                program[1] = noun
                program[2] = verb

                intcode_computer = IntcodeComputer(program)
                intcode_computer.run_until_termination()

                if intcode_computer.program[0] == 19690720:
                    self.part_two_result = 100 * noun + verb
                    return