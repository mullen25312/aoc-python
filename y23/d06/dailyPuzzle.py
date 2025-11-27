from utils.superDailyPuzzle import SuperDailyPuzzle

import math

def calculate_margin_of_error(time, record):
    button_pressed_max = math.floor(time/2 + math.sqrt(time**2/4-(record+1)))
    button_pressed_min = math.ceil(time/2 - math.sqrt(time**2/4-(record+1)))
    return button_pressed_max - button_pressed_min + 1

# advent of code 2023 day 6
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp= self.data.splitlines()
        times = [int(x) for x in tmp[0].split(":")[1].split()]
        records = [int(x) for x in tmp[1].split(":")[1].split()]
        self.parsed = (times, records)

    def part_one(self):
        (times, records) = self.parsed
        self.part_one_result = math.prod([calculate_margin_of_error(time, record) for (time, record) in zip(times, records)])

    def part_two(self):
        (times, records) = self.parsed
        (time, record) = map(lambda x: int(''.join([str(y) for y in x])), (times, records))
        self.part_two_result = calculate_margin_of_error(time, record)
