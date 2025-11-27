from utils.superDailyPuzzle import SuperDailyPuzzle

import re

# regular expression for parsing input
reg_expr1 = r"(\d+)"
reg_expr2 = r"([a-z]:)"
reg_expr3 = r"([a-z][a-z]+)"


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        for line in self.data.splitlines():
            tmp = re.findall(reg_expr1, line)
            letter = re.findall(reg_expr2, line)[0][0]
            password = re.findall(reg_expr3, line)[0]
            line_dict = {"min": int(tmp[0]), "max": int(tmp[1]), "letter": letter, "password": password}
            self.parsed.append(line_dict)

    def part_one(self):
        cnt = 0
        for line in self.parsed:
            if line["min"] <= line["password"].count(line["letter"]) <= line["max"]:
                cnt = cnt + 1
        self.part_one_result = cnt

    def part_two(self):
        cnt = 0
        for line in self.parsed:
            if (line["password"][line["min"] - 1] == line["letter"]) ^ (line["password"][line["max"] - 1] == line["letter"]):
                cnt = cnt + 1
        self.part_two_result = cnt
