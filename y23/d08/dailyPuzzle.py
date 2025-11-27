from utils.superDailyPuzzle import SuperDailyPuzzle

from math import lcm

dir = {"L":0, "R":1}

def determine_cycle(instructions, nodes, pos, end_criteria):
    steps = 0
    while not end_criteria(pos):
        instruction = instructions[steps % len(instructions)]
        pos = nodes[pos][dir[instruction]]
        steps += 1
    return steps

# advent of code 2023 day 8
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        instructions = list(self.data.splitlines()[0])
        nodes = {line.split("=")[0].strip(): line.split("=")[1].strip()[1:-1].split(", ") for line in self.data.splitlines()[2:]}
        self.parsed = (instructions, nodes)

    def part_one(self):
        (instructions, nodes) = self.parsed

        self.part_one_result = determine_cycle(instructions, nodes, "AAA", lambda x: x == "ZZZ")

    def part_two(self):
        (instructions, nodes) = self.parsed

        poss = [s for s in nodes.keys() if "A" in s]
        self.part_two_result = lcm(*[determine_cycle(instructions, nodes, pos, lambda x: "Z" in x) for pos in poss])