from utils.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict
 
# advent of code 2023 day 4
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        for line in self.data.splitlines():
            tmp = [x.strip() for x in line.split(":")[1].split("|")]
            self.parsed.append(([int(x) for x in tmp[0].split(" ") if x.isnumeric()], [int(x) for x in tmp[1].split(" ") if x.isnumeric()]))

    def part_one(self):
        result = 0

        for card in self.parsed:
            won = set(card[0]).intersection(set(card[1]))
            if len(won) > 0: result += 2**(len(won)-1)

        self.part_one_result = result

    def part_two(self):
        cards = defaultdict(lambda: 0) 

        for idx, card in enumerate(self.parsed):
            cards[idx] += 1
            won = set(card[0]).intersection(set(card[1]))
            for tmp in range(1, len(won)+1):
                cards[idx+tmp] += cards[idx]    

        self.part_two_result = sum(cards.values())
