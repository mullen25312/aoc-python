from utils.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict
import copy

class Part:
    def __init__(self, x, m, a, s):
        self.x = x; self.m = m; self.a = a; self.s = s

property_dict = {"x": lambda p: p.x, "m": lambda p: p.m, "a": lambda p: p.a, "s": lambda p: p.s}

# advent of code 2023 day 19
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        parts = []
        workflows = defaultdict(lambda: [])
        workflows_finished = False
        for line in self.data.splitlines():
            if workflows_finished == False:
                if line == "": 
                    workflows_finished = True
                    continue
                name = line.split("{")[0]
                rules = line.split("{")[1][:-1]
                for rule in rules.split(","):
                    tmp = rule.split(":")
                    if len(tmp) == 2:
                        result =  tmp[1]
                        if ">" in tmp[0]:
                            (left, right) = (tmp[0].split(">")[0], int(tmp[0].split(">")[1]))
                            workflows[name].append((lambda p, l=left, r=right: property_dict[l](p) > r, result))
                        elif "<" in tmp[0]:
                            (left, right) = (tmp[0].split("<")[0], int(tmp[0].split("<")[1]))
                            workflows[name].append((lambda p, l=left, r=right: property_dict[l](p) < r, result))
                    else:
                        result = tmp[0]
                        workflows[name].append((lambda p, l=0, r=0: True, result))  
            else:
                x = int(line.split(",")[0].split("=")[1])
                m = int(line.split(",")[1].split("=")[1])
                a = int(line.split(",")[2].split("=")[1])
                s = int(line.split(",")[3].split("=")[1][:-1])
                parts.append(Part(x, m, a, s))
  

        self.parsed = (workflows, parts)

    def part_one(self):
        (workflows, parts) = self.parsed

        results = []
        for part in parts:
            workflow = "in"
            while workflow != "R" and workflow != "A":
                for idx, rule in enumerate(workflows[workflow]):
                    if rule[0](part):
                        workflow = rule[-1]
                        break
            results.append(workflow)

        self.part_one_result = sum([part.x + part.m + part.a + part.s for (part, result) in zip(parts, results) if result == "A"])

    def part_two(self):
        self.part_two_result = 0