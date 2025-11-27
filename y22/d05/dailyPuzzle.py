from utils.superDailyPuzzle import SuperDailyPuzzle

import copy
import re

# regular expressions for data parsing
reg_expr_one = r"[A-Z]|\s{4}" # first section (initial stacks)
reg_expr_two= r"move ([0-9]+) from ([0-9]+) to ([0-9]+)" # second section: procedure

# advent of code 2022 day 05
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)


    def parse(self):
        self.parsed = {"stacks": [], "procedure":[]}
        tmp = []

        # read and parse input data line by line: first section: initial stacks, second section: procedure
        lines_iter = iter([line for line in self.data.splitlines()])

        line = next(lines_iter)
        while line[0:2]!= " 1": # stop after first second
            tmp.append([x.strip() for x in re.findall(reg_expr_one, line)])
            line = next(lines_iter)
        next(lines_iter)
        
        # continue with second section
        while True:
            try:
                line = next(lines_iter)
                self.parsed["procedure"].append([int(x) for x in list(re.findall(reg_expr_two, line)[0])])
            except StopIteration:
                break
        
        # parse row-major stack information into col-major
        self.parsed["stacks"] = [[] for x in range(len(tmp[0]))]
        for row in reversed(tmp):
            for idx, crate in enumerate(row):
                if crate != "":
                    self.parsed["stacks"][idx].append(crate)

    def part_one(self):
        stacks = copy.deepcopy(self.parsed["stacks"])
        for step in self.parsed["procedure"]:
            for idx in range(step[0]):
                tmp = stacks[step[1]-1].pop()
                stacks[step[2]-1].append(tmp)

        self.part_one_result = ''.join([x[-1] for x in stacks])

    def part_two(self):
        stacks = copy.deepcopy(self.parsed["stacks"])
        for step in self.parsed["procedure"]:
            tmp = [stacks[step[1]-1].pop() for _ in range(step[0])]
            stacks[step[2]-1].extend(reversed(tmp))

        self.part_two_result = ''.join([x[-1] for x in stacks])
