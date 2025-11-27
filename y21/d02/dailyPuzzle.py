from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [(line.split(" ")[0], int(line.split(" ")[1])) for line in self.data.splitlines()]

    def part_one(self):
        pos, depth = 0, 0

        for move in self.parsed:
            # algebraic solution
            pos += (move[0] == "forward") * move[1]
            depth += ((move[0] == "down") - (move[0] == "up")) * move[1]

            # case solution
            # if move[0] == "forward":
            #     pos += move[1]
            # elif move[0] == "down":
            #     depth += move[1]
            # elif move[0] == "up":
            #     depth -= move[1]
            # else:
            #     pass

        self.part_one_result = pos * depth

    def part_two(self):
        pos, depth, aim = 0, 0, 0

        for move in self.parsed:
            # algebraic solution
            aim += ((move[0] == "down") - (move[0] == "up")) * move[1]
            pos += (move[0] == "forward") * move[1]
            depth += (move[0] == "forward") * (aim * move[1])

            # if move[0] == "forward":
            #     pos += move[1]
            #     depth += aim * move[1]
            # elif move[0] == "down":
            #     aim += move[1]
            # elif move[0] == "up":
            #     aim -= move[1]
            # else:
            #     pass

        self.part_two_result = pos * depth
