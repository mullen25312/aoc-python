from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations
# import shapely as sl

def area(pair): return (abs(pair[0][0]-pair[1][0])+1) * (abs(pair[0][1]-pair[1][1])+1)

def get_circumference_points(vertices):
    outline = []
    for p1, p2 in zip(vertices, vertices[1:]):
        if p1[0] == p2[0]:
            outline.extend([(p1[0], y) for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)])
        elif p1[1] == p2[1]:
            outline.extend([(x, p1[1]) for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)])  
        else:
            raise ValueError("only axis-aligned rectangles are supported")
    return outline


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

        get_bounding_box = lambda pts: (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))

        # coordinate system compression
        compressedX = {x: i for i, x in enumerate(sorted(set([x for x, _ in vertices])))}
        decompressedX = {i: x for i, x in enumerate(sorted(set([x for x, _ in vertices])))}
        compressedY = {y: i for i, y in enumerate(sorted(set([y for _, y in vertices])))}
        decompressedY = {i: y for i, y in enumerate(sorted(set([y for _, y in vertices])))}

        # coordinate transformations
        compressCoords = lambda pts: [(compressedX[p[0]], compressedY[p[1]]) for p in pts]
        decompressCoords = lambda pts: [(decompressedX[p[0]], decompressedY[p[1]]) for p in pts]

        # compressed vertices
        compressedVertices = compressCoords([*vertices, vertices[0]])  # close the polygon

        # easy approach unsing shapely
        # polygon = sl.Polygon(compressedVertices)
        # self.part_two_result = max(area(decompressCoords((p1, p2))) * polygon.contains(sl.box(*get_bounding_box((p1, p2)))) for p1, p2 in combinations(compressedVertices, 2))

        # alternative approach without shapely
        outline = set(get_circumference_points(compressedVertices))
        
        res = 0
        for p1, p2 in combinations(compressedVertices, 2):
            if p1[0] == p2[0] or p1[1] == p2[1]: continue
            tmp = area(decompressCoords((p1, p2)))
            if tmp <= res: continue

            x1,y1,x2,y2 = get_bounding_box((p1, p2))
            interior_box_points = get_circumference_points([(x1+1,y1+1),(x2-1,y1+1),(x2-1,y2-1),(x1+1,y2-1), (x1+1,y1+1)])

            for pt in interior_box_points:
                if pt in outline:
                    break
            else:
                res = tmp

        self.part_two_result = res
        