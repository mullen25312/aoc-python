from utils.superDailyPuzzle import SuperDailyPuzzle
import copy


class Handheld:
    def __init__(self, program):
        self.acc = 0
        self.ip = 0
        self.ips = set()
        self.program = program

    def run(self):
        while self.ip not in self.ips:
            if self.ip == len(self.program):
                return True
            self.ips.add(self.ip)
            instruction = self.program[self.ip][0]
            argument = self.program[self.ip][1]

            if instruction == "acc":
                self.acc += argument
                self.ip += 1
            elif instruction == "jmp":
                self.ip += argument
            else:
                self.ip += 1

        return False

    def get_acc(self):
        return self.acc


# advent of code 2020 day 8
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        
        for line in self.data.splitlines():
            instruction = line.split(" ")[0]
            argument = int(line.split(" ")[1])
            self.parsed.append([instruction, argument])

    def part_one(self):
        mHandheld = Handheld(self.parsed)
        mHandheld.run()
        self.part_one_result = mHandheld.get_acc()

    def part_two(self):
        for idx in range(len(self.parsed)):
            instructions = copy.deepcopy(self.parsed)
            if instructions[idx][0] == "nop":
                instructions[idx][0] = "jmp"
            elif instructions[idx][0] == "jmp":
                instructions[idx][0] = "nop"
            else:
                continue

            mHandheld = Handheld(instructions)
            if mHandheld.run():
                self.part_two_result = mHandheld.get_acc()
                return

        self.part_two_result = "unsuccessful"