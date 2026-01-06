from utils.superDailyPuzzle import SuperDailyPuzzle

def invalids(n, repeat=2):
    result = []
    
    # for each possible sequence length (up to n//2 since we need at least 2 repetitions)
    for seq_len in range(1, n // 2 + 1):
        
        # generate all possible sequences of this length (no leading zeros)       
        for seq_val in range(10**(seq_len-1), 10**seq_len):
                        
            # add all valid repetitions up to n digits and at most repeat times
            for idx in range(2, repeat+1):
                current_str = str(seq_val) * idx
                if len(current_str) > n: break
                result.append(int(current_str))

    # remove duplicates and return sorted list
    return sorted(list(set(result)))

def check(invalids, spans):
    res = 0
    for num in invalids:
        for span in spans:
            if num in range(span[0], span[1] + 1):
                res += num
                break
    return res

# advent of code 2025 day 2
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [(int(span.split("-")[0]), int(span.split("-")[1])) for span in self.data.split(",")]

    def part_one(self):
        spans = self.parsed
        self.part_one_result = check(invalids(10,2), spans)

    def part_two(self): 
        spans = self.parsed
        self.part_two_result = check(invalids(10, 10), spans)