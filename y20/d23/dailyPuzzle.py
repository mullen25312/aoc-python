from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 23
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [int(n) for n in self.data.strip()]

    def part_one(self):
        N = len(self.parsed)

        cups = {}
        for idx, cup in enumerate(self.parsed):
            cups[cup] = self.parsed[(idx + 1)  % N]

        current = self.parsed[0]

        for _ in range(100):
            # remove pick up
            tmp = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
            cups[current] = cups[cups[cups[cups[current]]]]
            
            # destination
            diff = -1
            while (current+diff) % (N+1) not in cups.keys() or (current+diff) % (N+1) in tmp:
                diff -= 1
            dest = (current+diff) % (N+1)

            # insert pick up
            cups[tmp[2]] = cups[dest]
            cups[dest] = tmp[0]
            
            # prepare next round
            current = cups[current]

        result = [1]
        for _ in range(len(cups)-1):
            result.append(cups[result[-1]])
        self.part_one_result = ''.join([str(n) for n in result[1:]])
        
    def part_two(self):
        cups = {}
        for idx, cup in enumerate(self.parsed):
            if idx < len(self.parsed)-1:
                cups[cup] = self.parsed[(idx + 1)]
            else:
                cups[cup] = idx + 2
        
        M = 1000000
        for idx in range(10, M+1):
            cups[idx] = (idx+1)

        cups[M] = self.parsed[0]

        N = len(cups)
        current = self.parsed[0]
        
        for _ in range(10000000):
            # remove pick up
            tmp = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
            cups[current] = cups[cups[cups[cups[current]]]]
            
            # destination
            diff = -1
            while (current+diff) % (N+1) not in cups.keys() or (current+diff) % (N+1) in tmp:
                diff -= 1
            dest = (current+diff) % (N+1)

            # insert pick up
            cups[tmp[2]] = cups[dest]
            cups[dest] = tmp[0]
            
            # prepare next round
            current = cups[current]
            
        self.part_two_result = cups[1]*cups[cups[1]]