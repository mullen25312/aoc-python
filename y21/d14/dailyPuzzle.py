from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import product
from collections import defaultdict


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = {"template": None, "insertions": None}

        tmp = self.data.split("\n\n")
        self.parsed["template"] = tmp[0]
        self.parsed["insertions"] = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in tmp[1].splitlines()}

    def part_one(self):
        polymer = list(self.parsed["template"])
        number_of_steps = 10

        # insertions
        for idx in range(number_of_steps):
            cursor = 0
            while cursor < len(polymer) - 1:
                tmp = polymer[cursor] + polymer[cursor + 1]
                if tmp in self.parsed["insertions"].keys():
                    polymer.insert(cursor + 1, self.parsed["insertions"][tmp])
                    cursor += 1
                cursor += 1

        # histogram
        hist = dict(product(polymer, [0]))
        for element in hist.keys():
            hist[element] = "".join(polymer).count(element)

        self.part_one_result = hist[sorted(hist, key=hist.get)[-1]] - hist[sorted(hist, key=hist.get)[0]]

    def part_two(self):
        polymer = list(self.parsed["template"])
        number_of_steps = 40

        pair_hist = defaultdict(lambda: 0)
        for cursor in range(len(polymer) - 1):
            pair_hist[polymer[cursor] + polymer[cursor + 1]] += 1

        for idx in range(number_of_steps):
            # tmp = hist.copy()
            tmp = defaultdict(lambda: 0)
            for pair in pair_hist.keys():
                new_pair0 = pair[0] + self.parsed["insertions"][pair]
                new_pair1 = self.parsed["insertions"][pair] + pair[1]
                tmp[new_pair0] += pair_hist[pair]
                tmp[new_pair1] += pair_hist[pair]
                # tmp[pair] = 0
            pair_hist = tmp

        hist = defaultdict(lambda: 0)
        for pair in pair_hist.keys():
            hist[pair[0]] += pair_hist[pair]
            hist[pair[1]] += pair_hist[pair]

        hist = {k: v // 2 for k, v in hist.items()}
        hist[polymer[0]] += 1
        hist[polymer[-1]] += 1

        # print(hist)

        self.part_two_result = hist[sorted(hist, key=hist.get)[-1]] - hist[sorted(hist, key=hist.get)[0]]
