from utils.superDailyPuzzle import SuperDailyPuzzle


# advent of code 2022 day 08
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):

        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]

        self.parsed = []
        for line in lines:
            tmp = []
            for number in line:
                tmp.append(int(number))
            self.parsed.append(tmp)


    def part_one(self):
        N = len(self.parsed)
        M = len(self.parsed[0])

        result1 = [[False for tree in row] for row in self.parsed]

        # row-wise forward
        for idx1 in range(N):
            result1[idx1][0] = True
            tmp = self.parsed[idx1][0]
            for idx2 in range(1,M):
                if self.parsed[idx1][idx2] > tmp:
                    result1[idx1][idx2] = True
                    tmp = self.parsed[idx1][idx2] 

        # row-wise backward
        for idx1 in range(N):
            result1[idx1][M-1] = True
            tmp = self.parsed[idx1][M-1]
            for idx2 in range(1,M):
                if self.parsed[idx1][M-1-idx2] > tmp:
                    result1[idx1][M-1-idx2] = True
                    tmp = self.parsed[idx1][M-1-idx2] 

        # col-wise forward
        for idx1 in range(M):
            result1[0][idx1] = True
            tmp = self.parsed[0][idx1] 
            for idx2 in range(1,N):
                if self.parsed[idx2][idx1] > tmp:
                    result1[idx2][idx1] = True
                    tmp = self.parsed[idx2][idx1]

        # col-wise backwards
        for idx1 in range(M):
            result1[M-1][idx1] = True
            tmp = self.parsed[M-1][idx1] 
            for idx2 in range(1,N):
                if self.parsed[N-1-idx2][idx1] > tmp:
                    result1[N-1-idx2][idx1] = True
                    tmp = self.parsed[N-1-idx2][idx1]

        self.part_one_result = sum([tree for row in result1 for tree in row])

    def part_two(self):
        N = len(self.parsed)
        M = len(self.parsed[0])

        result2 = [[1 for tree in row] for row in self.parsed]

        for idx1, row in enumerate(self.parsed):
            for idx2, tree in enumerate(row):

                # look left
                tmp = 0
                for idx3 in range(idx2):
                    if self.parsed[idx1][idx2] > self.parsed[idx1][idx2-(idx3+1)]:
                        tmp += 1
                    else:
                        tmp += 1
                        break
                if tmp != 0:  result2[idx1][idx2] *= tmp 

                # look right
                tmp = 0
                for idx3 in range(M-1-idx2):
                    if self.parsed[idx1][idx2] > self.parsed[idx1][idx2+(idx3+1)]:
                        tmp += 1
                    else:
                        tmp += 1
                        break
                if tmp != 0: result2[idx1][idx2] *= tmp 

                # look up
                tmp = 0
                for idx3 in range(idx1):
                    if self.parsed[idx1][idx2] > self.parsed[idx1-(idx3+1)][idx2]:
                        tmp += 1
                    else:
                        tmp += 1
                        break
                if tmp != 0:  result2[idx1][idx2] *= tmp 

                # look down
                tmp = 0
                for idx3 in range(N-1-idx1):
                    if self.parsed[idx1][idx2] > self.parsed[idx1+(idx3+1)][idx2]:
                        tmp += 1
                    else:
                        tmp += 1
                        break
                if tmp != 0:  result2[idx1][idx2] *= tmp 
                

        self.part_two_result = max(max(x) for x in result2)
