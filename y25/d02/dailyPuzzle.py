from utils.superDailyPuzzle import SuperDailyPuzzle


def sgn(num): return -1 if num < 0 else 1

# advent of code 2025 day 2
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [(int(span.split("-")[0]), int(span.split("-")[1])) for span in self.data.split(",")]

    def part_one(self):
        spans = self.parsed

        res = 0
        for span in spans:
            for num in range(span[0], span[1] + 1): # for every number in given span
                if len(str(num)) % 2 == 0: # if length is odd cannot be invalid
                    if str(num)[:len(str(num))//2] == str(num)[len(str(num))//2:]: res += num # invalid if equal halves
        self.part_one_result = res

    def part_two(self): 
        spans = self.parsed

        res = 0
        for span in spans:
            for num in range(span[0], span[1] + 1): # for every number in given span
                for seq in range(1, len(str(num))//2 + 1): # for every possible sequence length
                    for offset in range(0, len(str(num))-seq, seq): # for every possible offset
                        if str(num)[offset:offset+seq] != str(num)[offset+seq:offset+2*seq]:
                            break
                    else: # completed full loop without breaking, so all offsets for a single sequence length matched
                        res += num
                        break # no need to check larger sequence lengths
        self.part_two_result = res