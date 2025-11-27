from utils.superDailyPuzzle import SuperDailyPuzzle

sin_table = {0: 0, 1: 1, 2: 0, 3: -1}
cos_table = {0: 1, 1: 0, 2: -1, 3: 0}


# advent of code 2020 day 12
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        
        for line in self.data.splitlines():
            self.parsed.append([line[0], int(line[1:])])

    def part_one(self):
        x, y, face = 0, 0, 0

        for instruction in self.parsed:
            com = instruction[0]
            arg = instruction[1]
            if com == "N":
                y += arg
            elif com == "S":
                y -= arg
            elif com == "E":
                x += arg
            elif com == "W":
                x -= arg
            elif com == "L":
                face = (face - int(arg / 90)) % 4
            elif com == "R":
                face = (face + int(arg / 90)) % 4
            elif com == "F":
                x += ((face + 1) % 2) * arg * (1 - face)
                y += (face % 2) * arg * (face - 2)

        self.part_one_result = abs(x) + abs(y)

    def part_two(self):
        dx, dy = 10, 1
        xs, ys = 0, 0

        for instruction in self.parsed:
            com = instruction[0]
            arg = instruction[1]
            if com == "N":
                dy += arg
            elif com == "S":
                dy -= arg
            elif com == "E":
                dx += arg
            elif com == "W":
                dx -= arg
            elif com == "L":
                angle = -int(arg / 90) % 4
                tmp = cos_table[angle] * dx + sin_table[angle] * dy
                dy = -sin_table[angle] * dx + cos_table[angle] * dy
                dx = tmp

            elif com == "R":
                angle = int(arg / 90) % 4
                tmp = cos_table[angle] * dx + sin_table[angle] * dy
                dy = -sin_table[angle] * dx + cos_table[angle] * dy
                dx = tmp

            elif com == "F":
                xs += arg * dx
                ys += arg * dy

        self.part_two_result = abs(xs) + abs(ys)