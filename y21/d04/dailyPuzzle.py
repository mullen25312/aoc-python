from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse random sequence
        self.parsed = {"sequence":[int(number) for number in self.data.splitlines()[0].split(',')]}
        
        # parse boards (have an integer +1 representation to use negative integers as marked numbers)
        self.parsed.update({"boards":[]})
        for lines_chunk in zip(*[iter(self.data.splitlines()[1:])]*6):
            tmp = []
            for line in lines_chunk[1:]:
                tmp.append([int(line[idx:idx+2])+1 for idx in range(0, len(line), 3)])
            self.parsed["boards"].append(np.array(tmp))

    def part_one(self):
        # for every random number check every board
        for number in self.parsed["sequence"]:
            for board in self.parsed["boards"]:
                board[board==number+1] *= -1 # mark number by negative integer

                # check bingo
                if any(all(row<0) for row in board) | any(all(col<0) for col in board.transpose()):
                    self.part_one_result = sum(abs(board[board>0]-1))*number
                    return

        self.part_one_result = "no bingo"
        return

    def part_two(self):
        not_won = set(range(len(self.parsed["boards"])))
        
        # for every random number check every board
        for number in self.parsed["sequence"]:
            for idx, board in enumerate(self.parsed["boards"]):
                board[board==number+1] *= -1 # mark number by negative integer

                # check bingo 
                if (idx in not_won) & (any(all(row<0) for row in board) | any(all(col<0) for col in board.transpose())):
                    if len(not_won)==1:
                        self.part_two_result = sum(abs(board[board>0]-1))*number
                        return
                    else:
                        not_won.remove(idx)

        self.part_two_result = "At least one board does never win"
        return
