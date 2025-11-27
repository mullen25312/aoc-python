from utils.superDailyPuzzle import SuperDailyPuzzle
import math
from collections import OrderedDict

def in_line_of_sight(vec1, vec2):
    # only vectors in the same quadrant can be in line of sight
    if ((vec1[0] >= 0) == (vec2[0] >= 0)) and ((vec1[1] >= 0) == (vec2[1] >= 0)):
        # check for linear dependency
        if vec1[0] != 0 and vec2[0] != 0:
            if vec1[1] / vec1[0] == vec2[1] / vec2[0]:
                return True
        if vec1[0] == 0 and vec2[0] == 0:
            return True
        else:
            return False
    else:
        return False

# advent of code 2019 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)
        self.astroid_map_dict = {}

    def parse(self):
        # read input data
        lines = self.data.splitlines()
        # and save as dictionary with astroid positions as keys
        for y, line in enumerate(lines):
            for x, pos in enumerate(line):
                if pos == "#":
                    self.astroid_map_dict[(x, y)] = []

    def part_one(self):
        # look through all astroids
        for astroid in self.astroid_map_dict:
            # order other astroids by distance w.r.t. considered astroid
            other_astroids = OrderedDict(
                sorted(
                    self.astroid_map_dict.items(),
                    key=lambda item: (item[0][0] - astroid[0]) ** 2
                    + (item[0][1] - astroid[1]) ** 2,
                )
            )
            # delete first astroid with distance zero because it is itself
            other_astroids.popitem(last=False)

            # go through all other astroids ordered by distance
            for other_astroid in other_astroids:
                # assume it is not blocked
                self.astroid_map_dict[astroid].append(other_astroid)

                # and check against all other already in line of sight
                vec1 = (other_astroid[0] - astroid[0], other_astroid[1] - astroid[1])
                for los_astroid in self.astroid_map_dict[astroid][:-1]:
                    vec2 = (los_astroid[0] - astroid[0], los_astroid[1] - astroid[1])
                    if in_line_of_sight(vec1, vec2):
                        # if in line of sight dismiss
                        self.astroid_map_dict[astroid].pop()
                        break

        # find astroid position with most line of sight astroids for monitoring station
        monitoring_station = max(
            self.astroid_map_dict.keys(),
            key=(lambda astroid: len(self.astroid_map_dict[astroid])),
        )

        # return number of most line of sight astroids
        self.part_one_result = len(self.astroid_map_dict[monitoring_station])


    def part_two(self):
        # what is the astroid position with most line of sight astroids again
        monitoring_station = max(
            self.astroid_map_dict.keys(),
            key=(lambda astroid: len(self.astroid_map_dict[astroid])),
        )

        # lets vaporize them all
        vaporized = []
        while len(self.astroid_map_dict) != 1:  # until monitoring station is left
            # arrange astroid in line of sight in clockwise (reverse mathematical) order
            # rotate coordinate frame by 90 deg because laser fires along y-axis first
            self.astroid_map_dict[monitoring_station].sort(
                key=lambda item: math.atan2(
                    -(item[0] - monitoring_station[0]) - 0.0000001,  # corr: above first
                    +(item[1] - monitoring_station[1]),
                ),
            )
            # vaporize each astroid in that order
            for astroid in self.astroid_map_dict[monitoring_station]:
                vaporized.append(astroid)
                self.astroid_map_dict.pop(astroid)
            self.astroid_map_dict[monitoring_station] = []

            # determine new astroids in line of sight
            # order other astroids by distance w.r.t. considered astroid
            other_astroids = OrderedDict(
                sorted(
                    self.astroid_map_dict.items(),
                    key=lambda item: (item[0][0] - monitoring_station[0]) ** 2
                    + (item[0][1] - monitoring_station[1]) ** 2,
                )
            )
            # delete first astroid with distance zero because it is itself
            other_astroids.popitem(last=False)

            # go through all other astroids ordered by distance
            for other_astroid in other_astroids:
                # assume it is not blocked
                self.astroid_map_dict[monitoring_station].append(other_astroid)

                # and check against all other already in line of sight
                vec1 = (
                    other_astroid[0] - monitoring_station[0],
                    other_astroid[1] - monitoring_station[1],
                )
                for los_astroid in self.astroid_map_dict[monitoring_station][:-1]:
                    vec2 = (
                        los_astroid[0] - monitoring_station[0],
                        los_astroid[1] - monitoring_station[1],
                    )
                    if in_line_of_sight(vec1, vec2):
                        # if in line of sight dismiss
                        self.astroid_map_dict[monitoring_station].pop()
                        break

        # return result: multiply its X coordinate by 100 and then add its Y coordinate
        self.part_two_result = vaporized[200 - 1][0] * 100 + vaporized[200 - 1][1]