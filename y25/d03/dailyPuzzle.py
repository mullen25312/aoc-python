from utils.superDailyPuzzle import SuperDailyPuzzle

# function to select batteries maximizing total joltage for a given number of batteries
def maximum_joltage(bank, number_of_batteries):
    batteries = [None] * number_of_batteries # prepare battery list
    min_idx = 0 # index to start searching from
    for idx in range(0, number_of_batteries): # for each battery to be selected
        max_idx = len(bank)-(number_of_batteries-1-idx) # index to stop searching at
        batteries[idx] = max(bank[min_idx:max_idx]) # select maximum joltage battery
        min_idx = min_idx +bank[min_idx:max_idx].index(batteries[idx]) + 1 # update index to start searching from
    return sum([battery*(10**idx) for idx, battery in enumerate(batteries[::-1])]) # calculate total joltage


# advent of code 2025 day 3
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [[int(battery) for battery in bank ] for bank in self.data.splitlines()]

    def part_one(self):
        # choose 2 batteries from bank maximizing joltage for part one
        self.part_one_result = sum(maximum_joltage(bank, 2) for bank in self.parsed) 

    def part_two(self):
        # choose 12 batteries from bank maximizing joltage for part two
        self.part_two_result = sum(maximum_joltage(bank, 12) for bank in self.parsed) 