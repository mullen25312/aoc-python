from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2025 day x
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):

        patterns = []
        regions = []

        for idx in range(0,6):
            patterns.append(self.data.splitlines()[idx*5+1:idx*5+4])

        for line in self.data.splitlines()[30:]:
            size = tuple(int(x) for x in line.split(':')[0].split('x'))
            quanities = [int(x) for x in line.split(':')[1][1:].split(' ')]
            regions.append((size, quanities))

        self.parsed = patterns, regions
    
    def part_one(self):
        patterns, regions = self.parsed

        possible_count = []
        impossible_count = []

        pattern_count = [sum(row.count('#') for row in pattern) for pattern in patterns]
        
        for idx, region in enumerate(regions):
            # check if all pattern can even fit in region assuming they interlook perfectly, if not then impossible
            if sum([pattern_count[i] * region[1][i] for i in range(6)]) > region[0][0] * region[0][1]: 
                impossible_count.append(idx)

            # check if area is big enough to fit pattern next to each other without need for overlap
            if (sum(region[1])*9 <= region[0][0] * region[0][1]):
                possible_count.append(idx)

        # print(f"possible: {len(possible_count)}, impossible: {len(impossible_count)}, unknown: {len(regions)-len(possible_count) - len(impossible_count)}")
        # print(f"solution only valied, if intersection of both is empty: {set(impossible_count) & set(possible_count)}")

        sols = range(len(possible_count), len(regions) - len(impossible_count) + 1)
        # print(f"possible solutions: {list(solutions)}")

        self.part_one_result = sols[0] # take the lower bound as guess

    def part_two(self): 
        self.part_two_result = 0