from utils.superDailyPuzzle import SuperDailyPuzzle

import math

# advent of code 2025 day 6
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):

        char_matrix = []
        cols = [[] for _ in range(sum([1 if x in "+*" else 0 for x in self.data.splitlines()[-1]]))]
        for line in self.data.splitlines()[:-1]:
            for idx, number in enumerate(line.split()): cols[idx].append(int(number)) # columns of numbers for part one
            char_matrix.append(list(line+' ')) # char matrix with spaces as padding for part two
        operators = [char for char in self.data.splitlines()[-1] if char in "+*"]    
        
        self.parsed = char_matrix, cols, operators

    def part_one(self):
        _, cols, operators = self.parsed
        
        res = [0]*len(operators)

        for idx, operator in enumerate(operators):
            if operator == "+":
                res[idx] = sum(cols[idx])
            elif operator == "*":
                res[idx] = math.prod(cols[idx])
                
        self.part_one_result = sum(res)

    def part_two(self): 
        char_matrix, cols, operators = self.parsed

        max_lengths = [len(str(x)) + 1 for x in [max(col) for col in cols]]
        res = [0]*len(operators)

        for idx, length in enumerate(max_lengths):
            if operators[idx] == "+":
                res[idx] = sum([int(''.join([char_matrix[y][sum(max_lengths[:idx]) + col] for y in range(len(char_matrix))])) for col in range(length-1)])
            elif operators[idx] == "*":
                res[idx] = math.prod([int(''.join([char_matrix[y][sum(max_lengths[:idx]) + col] for y in range(len(char_matrix))])) for col in range(length-1)])

        self.part_two_result = sum(res)