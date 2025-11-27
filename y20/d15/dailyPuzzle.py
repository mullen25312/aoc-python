from utils.superDailyPuzzle import SuperDailyPuzzle


# advent of code 2020 day 15
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(n) for n in self.data.strip().split(',')]

    def part_one(self):
        spoken_dict = {}
        last = 0
        for idx, number in enumerate(self.parsed[:-1]):
            spoken_dict[number] = idx
        last = self.parsed[-1]

        N = 2020
        spoken = 0
        for idx in range(len(spoken_dict)-1, N-2):
            if last in spoken_dict.keys():
                spoken = idx+1 - spoken_dict[last] 
            else: 
                spoken = 0

            spoken_dict[last] = idx+1 
            last = spoken

        self.part_one_result = spoken

    def part_two(self):
        spoken_dict = {}
        last = 0
        for idx, number in enumerate(self.parsed[:-1]):
            spoken_dict[number] = idx
        last = self.parsed[-1]

        N = 30000000
        spoken = 0
        for idx in range(len(spoken_dict)-1, N-2):
            if last in spoken_dict.keys():
                spoken = idx+1 - spoken_dict[last] 
            else: 
                spoken = 0

            spoken_dict[last] = idx+1 
            last = spoken

        self.part_two_result = spoken