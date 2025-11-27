from utils.superDailyPuzzle import SuperDailyPuzzle
from collections import defaultdict
import copy

def myRange(number1, number2):
    minimum = min(number1, number2)
    maximum = max(number1, number2)
    return list(range(minimum, maximum+1))

# advent of code 2022 day 14
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]

        # parse grid of rocks
        self.parsed = defaultdict(lambda: 0)
        for line in lines:
            points = line.split(" -> ")
            tmp0 = [int(x) for x in points.pop(0).split(",")]
            for point in points:
                tmp1 = [int(x) for x in point.split(",")]
                if tmp0[0] == tmp1[0]:
                    for idx in myRange(tmp0[1], tmp1[1]):
                        self.parsed[(tmp0[0], idx)] = 1
                if tmp0[1] == tmp1[1]:
                    for idx in myRange(tmp0[0], tmp1[0]):
                        self.parsed[(idx, tmp0[1])] = 1       
                tmp0 = tmp1
        
    def part_one(self):
        rocks = copy.deepcopy(self.parsed)
        abyss = max(rocks.keys(), key = lambda x: x[1])[1]

        stop = False; idx = -1
        while not stop:
            idx += 1
            sand= [500,0]
            while True:
                # check if it falls forever and set stop flag if yes
                if sand[1] > abyss:
                    stop = True
                    break
                # check if it can pour down
                elif rocks[(sand[0], sand[1]+1)] == 0:
                    sand[1] += 1
                    continue
                # check if it can pour down/left
                elif rocks[(sand[0]-1, sand[1]+1)] == 0:
                    sand[0] -= 1
                    sand[1] += 1
                    continue
                # check if it can pour down/right
                elif rocks[(sand[0]+1, sand[1]+1)] == 0:
                    sand[0] += 1
                    sand[1] += 1
                    continue
                else:
                    rocks[(sand[0], sand[1])] = 2
                    break

        self.part_one_result = idx

    def part_two(self):
        rocks = copy.deepcopy(self.parsed)
        abyss = max(rocks.keys(), key = lambda x: x[1])[1] + 2

        stop = False; idx = 0
        while not stop:
            idx += 1
            sand= [500,0]
            while True:
                # check if floor is reached
                if sand[1] == abyss-1:
                    rocks[(sand[0], sand[1])] = 2
                    break
                # check if it can pour down
                elif rocks[(sand[0], sand[1]+1)] == 0:
                    sand[1] += 1
                    continue
                # check if it can pour down/left
                elif rocks[(sand[0]-1, sand[1]+1)] == 0:
                    sand[0] -= 1
                    sand[1] += 1
                    continue
                # check if it can pour down/right
                elif rocks[(sand[0]+1, sand[1]+1)] == 0:
                    sand[0] += 1
                    sand[1] += 1
                    continue
                else:
                    if sand == [500,0]: stop = True # check if sand reached initial point and set stop flag if yes
                    rocks[(sand[0], sand[1])] = 2
                    break

        self.part_two_result = idx
