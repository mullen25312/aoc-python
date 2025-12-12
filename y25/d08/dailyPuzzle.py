from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations

def distance(pair0, pair1):
    return (pair0[0]-pair1[0])**2 + (pair0[1]-pair1[1])**2 + (pair0[2]-pair1[2])**2

def find_pair_index(res_sets, pair):
    for tmp, res_set in enumerate(res_sets):
        if pair in res_set: return tmp
    return None

def connect_pairs(pair0, pair1, res_sets):
    pair0_index = find_pair_index(res_sets, pair0)
    pair1_index = find_pair_index(res_sets, pair1)

    if pair0_index is None and pair1_index is None:
        res_sets.append(set([pair0, pair1]))
    elif pair0_index is not None and pair1_index is None:
        res_sets[pair0_index].add(pair1)
    elif pair0_index is None and pair1_index is not None:
        res_sets[pair1_index].add(pair0)
    elif pair0_index != pair1_index:
        res_sets[pair0_index] = res_sets[pair0_index].union(res_sets[pair1_index])
        res_sets.pop(pair1_index)

# advent of code 2025 day 8
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [tuple(int(x) for x in line.split(',')) for line in self.data.splitlines()]
    
    def part_one(self):
        coordinates = self.parsed
        number_of_conncections = 1000 if len(coordinates) > 20 else 10

        res_sets = []
        for pair0, pair1 in sorted(combinations(coordinates, 2), key=lambda pair: distance(*pair))[0:number_of_conncections]:
            connect_pairs(pair0, pair1, res_sets)
            
        sizes = sorted([len(res_set) for res_set in res_sets], reverse=True)
        self.part_one_result = sizes[0] * sizes[1] * sizes[2]

    def part_two(self): 
        coordinates = self.parsed

        res_sets = []
        for pair0, pair1 in sorted(combinations(coordinates, 2), key=lambda pair: distance(*pair)):
            connect_pairs(pair0, pair1, res_sets)

            if len(res_sets[0]) == len(coordinates): 
             res = pair0[0]*pair1[0]
             break
            
        self.part_two_result = res