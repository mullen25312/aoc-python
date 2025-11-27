from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import product

# def convert_arrangements(arrangement):
#     n = len(arrangement)
#     mask = sum([2**(len(arrangement)-idx-1) for (idx, x) in enumerate(arrangement) if x=="?"])
#     damaged = sum([2**(len(arrangement)-idx-1) for (idx, x) in enumerate(arrangement) if x!="#"])

#     # x = damaged
#     # while tmp < 2**n:
#     #     # print((r'{0:0'+str(n)+r'b}').format(tmp))
#     #     x = ((x | ~mask) + 1) & mask

#     # print(bin(mask))

def generate_combinations(inp):
    ret = []
    for idx, i in enumerate(inp):
        if i == '?':
            for rest in generate_combinations(inp[idx+1:]):
                ret.append(inp[:idx] + '.' + rest)
                ret.append(inp[:idx] + '#' + rest)
            break
    else:
        return [inp]
    return ret
    
# advent of code 2023 day 12
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        arrangements = []
        groups = []

        tmp = self.data.splitlines()
        for line in tmp:
            arrangements.append(generate_combinations(line.split(" ")[0]))
            groups.append([int(x) for x in line.split(" ")[1].split(",")])

        self.parsed = (arrangements, groups)

    def part_one(self):
        (arrangements, groups) = self.parsed

        results = []
        for x, line in enumerate(arrangements):
            result = 0
            for arrangement in line:
                test = True
                tmp = [x for x in arrangement.split('.') if x!= ""]
                if len(tmp) == len(groups[x]):
                    for idx, groupsize in enumerate(groups[x]):
                        if len(tmp[idx]) != groupsize: test = False
                else: test = False
                if test == True: result += 1
            results.append(result)

        self.part_one_result = sum(results)

    def part_two(self):
        self.part_two_result = 0