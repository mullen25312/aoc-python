from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

start2end = {"(": ")", "[": "]", "{": "}", "<": ">"}

score_table_one = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_table_two = {"(": 1, "[": 2, "{": 3, "<": 4}


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = [line for line in self.data.splitlines()]
        pass

    def part_one(self):
        score = 0
        for line in self.parsed:
            tmp = []
            corrupted = False
            for char in line:
                if corrupted:
                    break
                else:
                    if char in start2end.keys():
                        tmp.append(char)
                    elif char == start2end[tmp[-1]]:
                        tmp.pop()
                    else:
                        # print(f"{line} - Expected {start2end[tmp[-1]]}, but found {char} instead.")
                        score += score_table_one[char]
                        corrupted = True

        self.part_one_result = score

    def part_two(self):
        scores = []
        for line in self.parsed:
            tmp = []
            score = 0
            corrupted = False
            for char in line:
                if corrupted:
                    break
                else:
                    if char in start2end.keys():
                        tmp.append(char)
                    elif char == start2end[tmp[-1]]:
                        tmp.pop()
                    else:
                        corrupted = True

            if not corrupted:
                for char in reversed(tmp):
                    score = score * 5 + score_table_two[char]
                scores.append(score)

        self.part_two_result = sorted(scores)[len(scores) // 2]
