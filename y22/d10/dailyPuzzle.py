from utils.superDailyPuzzle import SuperDailyPuzzle

class CathodeRayComputer:
    def __init__(self):
        self.history = [1]

    def noop(self):
        self.history.append(self.history[-1])

    def addx(self, value):
        self.noop()
        self.history.append(self.history[-1] + value)

    def getSignalStrength(self):
        return sum([self.history[cycle-1]*cycle for cycle in range(20, len(self.history), 40)])

    def renderScreen(self):
        output = ""
        for idx in range(0,len(self.history)-1):
            if idx > 0 and idx % 40 == 0: output += "\n"
            output += "#" if self.history[idx] - 1 <= idx % 40  <= self.history[idx] + 1 else "."
        return output

# advent of code 2022 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]

        # run cathode-ray computer
        self.parsed = CathodeRayComputer()
        for line in lines:
            command = line.split(" ")
            if command[0] == "noop":
                self.parsed.noop()
            elif command[0] == "addx" and len(command) == 2:
                self.parsed.addx(int(command[1]))

    def part_one(self):
        self.part_one_result = self.parsed.getSignalStrength()

    def part_two(self):
        self.part_two_result = "EKRHEPUZ"
