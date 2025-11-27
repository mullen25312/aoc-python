from utils.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict

dir_dict = {"north": 0, "west": 1, "south": 2, "east": 3}
reflexion_dict_slash = {dir_dict["north"]: dir_dict["east"], dir_dict["east"]: dir_dict["north"], dir_dict["west"]: dir_dict["south"], dir_dict["south"]: dir_dict["west"]}
reflexion_dict_backslash = {dir_dict["north"]: dir_dict["west"], dir_dict["west"]: dir_dict["north"], dir_dict["east"]: dir_dict["south"], dir_dict["south"]: dir_dict["east"]}

class Beam:
    def __init__(self, x, y, dir):
        self.x = x; self.y = y; self.dir = dir

def propagate_beam(layout, start_beam):
    (n, m) = (len(layout), len(layout[0]))

    beams = [start_beam]
    energized = defaultdict(lambda: [])

    # while there is a beam left to propagate
    while len(beams) != 0:

        # next position
        beams[0].y += ((beams[0].dir % 2) == 0) * (beams[0].dir - 1)
        beams[0].x += ((beams[0].dir % 2) == 1) * (beams[0].dir - 2)

        # check if in range and beam has not already been followed, otherwise terminate beam
        if not ((0 <= beams[0].y < n) and (0 <= beams[0].x < m)) or beams[0].dir in energized[(beams[0].x, beams[0].y)]:
            beams.pop(0)
            continue
        else:
            energized[(beams[0].x, beams[0].y)].append(beams[0].dir)

        # next direction
        if layout[beams[0].y][beams[0].x] == "|":
            if beams[0].dir  == dir_dict["west"] or beams[0].dir == dir_dict["east"]:
                beams[0].dir = dir_dict["south"]
                beams.append(Beam(beams[0].x, beams[0].y, dir_dict["north"]))

        elif layout[beams[0].y][beams[0].x] == "-":
            if beams[0].dir == dir_dict["north"] or beams[0].dir == dir_dict["south"]:
                beams[0].dir = dir_dict["west"]
                beams.append(Beam(beams[0].x, beams[0].y, dir_dict["east"]))

        elif layout[beams[0].y][beams[0].x]  == "/": beams[0].dir = reflexion_dict_slash[beams[0].dir]
        elif layout[beams[0].y][beams[0].x]  == "\\": beams[0].dir = reflexion_dict_backslash[beams[0].dir]

    return energized

# advent of code 2023 day 16
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        layout = []
        for line in self.data.splitlines():
            layout.append(list(line))
        self.parsed = layout

    def part_one(self):
        layout = self.parsed
        start_beam = Beam(-1, 0, dir_dict["east"])
        self.part_one_result = len(propagate_beam(layout, start_beam))

    def part_two(self):
        layout = self.parsed

        (n, m) = (len(layout), len(layout[0]))
        start_beams = []
        for idx in range(n):
            start_beams.append(Beam(-1, idx, dir_dict["east"]))
            start_beams.append(Beam( m, idx, dir_dict["west"]))
        for idx in range(m):
            start_beams.append(Beam(idx, -1, dir_dict["south"]))
            start_beams.append(Beam(idx,  n, dir_dict["north"]))

        results = []
        for start_beam in start_beams:
            results.append(len(propagate_beam(layout, start_beam)))

        self.part_two_result = max(results)