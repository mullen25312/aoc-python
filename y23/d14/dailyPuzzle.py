from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
import copy

d = {".": 0, "#": -1, "O": 1}
inv_map = {v: k for k, v in d.items()}

def print_platform(platform):
    for row in platform:
        print(''.join([inv_map.get(x, 0) for x in row]))
    print("")

def tilt(platform):
    for row in platform:
        last = 0
        for idx, value in enumerate(row):
            if value == 1: 
                row[idx] = 0
                row[last] = 1
                last += 1
            elif value == -1: last = idx+1
    return platform

def tilt_north(platform):
    return np.transpose(tilt(np.transpose(platform)))
def tilt_west(platform):
    return tilt(platform)
def tilt_east(platform):
    return np.fliplr(tilt(np.fliplr(platform)))
def tilt_south(platform):
    return np.flipud(np.transpose(tilt(np.transpose(np.flipud(platform)))))

# advent of code 2023 day 14
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp = []
        for line in self.data.splitlines():
            tmp.append([d.get(x, 0) for x in line])

        self.parsed = np.array(tmp)

    def part_one(self):
        platform = copy.copy(self.parsed)
        self.part_one_result = sum([sum(row==1)*(idx+1) for (idx, row) in enumerate(np.flipud(tilt_north(platform)))])

    def part_two(self):
        platform = copy.copy(self.parsed)

        caches = []
        caches.append(copy.copy(platform))

        # print(str(0)+":")
        # print_platform(platform)

        offset = 0
        period = 0

        for idx in range(0, 1000000000):

            platform = tilt_north(platform)
            platform = tilt_west(platform)
            platform = tilt_south(platform)
            platform = tilt_east(platform)
            
            # print(str(idx+1)+":")
            # print_platform(platform)

            test = False
            for tmp, cache in enumerate(caches):
                if (cache == platform).all():
                    offset = tmp
                    period = len(cache) - offset -1
                    # print(tmp)
                    # print(idx)
                    test = True
            if test == True:
                break
            caches.append(copy.copy(platform))


        # print(offset)
        # print(idx+1)
        # print(period)
        # print((1000000000) % period)
        result_platform = caches[(1000000000 - offset) % period ]

        # for idx, cache in enumerate(caches):
        #     print(idx)
        #     print(sum([sum(row==1)*(idx+1) for (idx, row) in enumerate(np.flipud(cache))]))


        self.part_two_result = sum([sum(row==1)*(idx+1) for (idx, row) in enumerate(np.flipud(result_platform))])