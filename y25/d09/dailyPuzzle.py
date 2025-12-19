from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations
import shapely as sl

def area(pair): return (abs(pair[0][0]-pair[1][0])+1) * (abs(pair[0][1]-pair[1][1])+1)

# advent of code 2025 day 9
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in self.data.splitlines()]
    
    def part_one(self):
        self.part_one_result = area(sorted(combinations(self.parsed, 2), key=lambda pair: area(pair))[-1])

    def part_two(self): 
        vertices = self.parsed

        polygon = sl.Polygon(vertices)
        get_bounding_box = lambda pts: (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))
            
        self.part_two_result = max(area((p1, p2)) * polygon.contains(sl.box(*get_bounding_box((p1, p2)))) for p1, p2 in combinations(vertices, 2))