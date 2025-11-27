from utils.superDailyPuzzle import SuperDailyPuzzle
from utils.tree import Tree

# advent of code 2022 day 06
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        self.parsed =  lines = [int(line.strip()) for line in self.data.splitlines()]

    def part_one(self):
        N =  len(self.parsed)
        shuffle = list(range(0,N))

        result1 = [0 for x in range(0,N)]
        for idx, pos in enumerate(shuffle):
            result1[pos] = self.parsed[idx]
        # print(str(result1) + " --> " + str(shuffle))

        for idx, number in enumerate(self.parsed[0:7]):
            if idx == 6:
                pass
            tmp2 = shuffle[idx]
            tmp = (tmp2+number-1) % (N-1) +1
            for idx2, pos in enumerate(shuffle):
                if tmp > tmp2:
                    if tmp2 < pos <= tmp: shuffle[idx2] -= 1
                if tmp < tmp2:
                    if tmp <= pos < tmp2: shuffle[idx2] += 1
            shuffle[idx] = tmp

        result1 = [0 for x in range(0,N)]
        for idx, pos in enumerate(shuffle):
            result1[pos] = self.parsed[idx]
        # print(str(result1) + " --> " + str(shuffle))
        # print(shuffle)
            
        tmp = shuffle[self.parsed.index(0)] 
        # print((tmp+1000)%(N-1))
        # print(result1[(tmp+1000)%(N)])
        # print(result1[(tmp+2000)%(N)])
        # print(result1[(tmp+3000)%(N)])
        self.part_one_result = result1[(tmp+1000)%(N)] + result1[(tmp+2000)%(N)] + result1[(tmp+3000)%(N)]

    def part_two(self):
        self.part_two_result = 0
