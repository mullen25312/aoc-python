from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
import regex as re

written_numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def convert_number(input):
    if input in written_numbers.keys():
        return written_numbers[input]
    else:
        return input
        
# advent of code 2023 day 1
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = self.data.splitlines()

    def part_one(self):
        input = np.array(self.parsed)
        sum = 0
        for line in input:
            tmp = re.findall(r'\d', line)
            if len(tmp)>0: 
                # print(line + ": " + convert_number(tmp[0]) + convert_number(tmp[-1]))
                sum += int(tmp[0])*10 + int(tmp[-1])
        self.part_one_result = sum

    def part_two(self):
        input = np.array(self.parsed)
        sum = 0
        for line in input:
            tmp = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line,  overlapped=True)
            if len(tmp)>0:
                # print(line + ": " + convert_number(tmp[0]) + convert_number(tmp[-1]))
                sum += int(convert_number(tmp[0]))*10 + int(convert_number(tmp[-1]))
        self.part_two_result = sum
