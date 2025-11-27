from utils.superDailyPuzzle import SuperDailyPuzzle

# 1: Rock (A, X), 2: Paper (B, Y), 3: Scissor (C, Z)
hand2number = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
win_eval = {(1, 1): 3, (1, 2): 6, (1, 3): 0, (2, 1): 0, (2, 2): 3, (2, 3): 6, (3, 1): 6, (3, 2): 0, (3, 3): 3}

# 1: lose (0 points), 2: draw (3 points), 3: win (6 points)
what2play = {(1, 1): 3, (1, 2): 1, (1, 3): 2, (2, 1): 1, (2, 2): 2, (2, 3): 3, (3, 1): 2, (3, 2): 3, (3, 3): 1}
points = {1: 0, 2: 3, 3: 6}

# advent of code 2022 day 02
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = [line for line in self.data.splitlines()]
        self.parsed = [[hand2number[line.split(" ")[0]], hand2number[line.split(" ")[1]]] for line in lines]

    def part_one(self):
        self.part_one_result = sum([win_eval[(game[0], game[1])] + game[1] for game in self.parsed])

    def part_two(self):
        self.part_two_result = sum([what2play[(game[0], game[1])] + points[game[1]] for game in self.parsed])
