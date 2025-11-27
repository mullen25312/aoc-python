from utils.superDailyPuzzle import SuperDailyPuzzle


def populate_fishes(initial_population, days=18):
    cycles = 9
    fishes = {age: 0 for age in range(0, cycles)}

    for fish in initial_population:
        fishes[fish] += 1

    for _ in range(days):
        tmp = fishes[0]
        fishes[0] = 0
        for cycle in range(1, cycles):
            fishes[cycle - 1] = fishes[cycle]  #
            fishes[cycle] = 0
        fishes[cycles - 1] = tmp
        fishes[cycles - 1 - 2] += tmp

    return fishes


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = [int(number) for number in self.data.splitlines()[0].split(",")]

    def part_one(self):
        fishes = populate_fishes(self.parsed, days=80)
        self.part_one_result = sum([fishes[age] for age in fishes.keys()])

    def part_two(self):
        fishes = populate_fishes(self.parsed, days=256)
        self.part_two_result = sum([fishes[age] for age in fishes.keys()])
