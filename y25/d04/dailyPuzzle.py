from utils.superDailyPuzzle import SuperDailyPuzzle

from copy import deepcopy

adjecents = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


# advent of code 2025 day 4
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        diagram = set()
        for y, line in enumerate(self.data.splitlines()):
            for x, char in enumerate(line):
                if char == '@': diagram.add((x,y))
        self.parsed = diagram
    

    def part_one(self):
        diagram = deepcopy(self.parsed)

        res = 0
        for roll_of_paper in diagram:
            res += sum([1 if (roll_of_paper[0]+dx, roll_of_paper[1]+dy) in diagram else 0 for dx, dy in adjecents]) < 4
        self.part_one_result = res

    def part_two(self): 
        diagram = deepcopy(self.parsed)

        res = 0
        while (True):
            to_be_removed = set()
            for roll_of_paper in diagram:
                if sum([1 if (roll_of_paper[0]+dx, roll_of_paper[1]+dy) in diagram else 0 for dx, dy in adjecents]) < 4: 
                    res += 1
                    to_be_removed.add(roll_of_paper)  
            if len(to_be_removed) == 0: break  
            for item in to_be_removed: diagram.remove(item)       
        self.part_two_result = res