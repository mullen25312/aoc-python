from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2022 day 01
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = [line for line in self.data.splitlines()]

        self.parsed = [[]]
        elf_number = 0
        for line in self.data.splitlines():
            if line != "":
                self.parsed[elf_number].append(int(line))
            else:
                self.parsed.append([])
                elf_number += 1

        self.parsed.sort(key=lambda elf:-sum(elf))

    def part_one(self):
        self.part_one_result = sum(self.parsed[0])

    def part_two(self):
        self.part_two_result = sum([cal for elf in self.parsed[0:3] for cal in elf])