from utils.superDailyPuzzle import SuperDailyPuzzle

def process_beams(manifold):
    beams = [[0] * len(manifold[0])]
    beams[0][manifold[0].index("S")] = 1

    res = 0
    for row in manifold[1:]:
        tmp_beams = beams[-1].copy()
        for idx, val in enumerate(beams[-1]):
            if val > 0 and row[idx] == "^":
                res += 1
                tmp_beams[idx - 1] += val
                tmp_beams[idx] -= val
                tmp_beams[idx + 1] += val
        beams.append(tmp_beams)
    return beams, res

# advent of code 2025 day 7
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [list(line) for line in self.data.splitlines()][0::2]
    
    def part_one(self):
        manifold = self.parsed
        _, res = process_beams(manifold)
        self.part_one_result = res

    def part_two(self): 
        manifold = self.parsed
        beams, _ = process_beams(manifold)
        self.part_two_result = sum(beams[-1])