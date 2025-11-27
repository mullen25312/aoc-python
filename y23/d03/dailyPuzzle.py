from utils.superDailyPuzzle import SuperDailyPuzzle

import math
import numpy as np
import re
 
# advent of code 2023 day 3
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        parts = {}
        symbols = {}

        for idx, line in enumerate(self.data.splitlines()):
            p = re.compile(r'\b[0-9]+\b')
            tmp = list([(match.start(), match.group()) for match in p.finditer(line)])
            if tmp: parts[idx] = tmp

            s =  re.compile(r'\$|\#|\+|\*|\=|\@|\&|\%|\/|\-')
            tmp = list([(match.start(), match.group()) for match in s.finditer(line)])
            if tmp: symbols[idx] = tmp

        self.parts = parts
        self.symbols = symbols

    def part_one(self):
        (parts, symbols) = (self.parts, self.symbols)
        result = 0

        # iterate over lines of parts
        for line in parts:
            # iterate over parts per line
            for part in parts[line]:
                # check in adjacent lines if part has adjacent symbol
                included = False
                if (line-1) in symbols.keys():
                    for symbol in symbols[line-1]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])): 
                            included = True
                if (line) in symbols.keys():
                    for symbol in symbols[line]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])): 
                            included = True
                if (line+1) in symbols.keys():
                    for symbol in symbols[line+1]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])): 
                            included = True

                # if yes, add this part to result
                if included:
                    result += int(part[1])

        self.part_one_result = result

    def part_two(self):
        (parts, symbols) = (self.parts, self.symbols)
        result = 0

        # iterate over line in symbols
        for line in symbols:
            # iterate over symbol per line
            for symbol in symbols[line]:
                # collect in adjacent lines every adjacent part
                adjacent = []
                if (line-1) in parts.keys():
                    for part in parts[line-1]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])):
                            adjacent.append(part[1])
                if (line) in parts.keys():
                    for part in parts[line]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])):
                            adjacent.append(part[1])
                if (line+1) in parts.keys():
                    for part in parts[line+1]:
                        if (part[0]-1) <= symbol[0] <= (part[0] + len(part[1])):
                            adjacent.append(part[1])

                # if only two are adjacent, add product to result
                if len(adjacent) == 2:
                    result += int(adjacent[0]) * int(adjacent[1])

        self.part_two_result = result
