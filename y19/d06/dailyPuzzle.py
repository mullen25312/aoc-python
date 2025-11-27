from utils.superDailyPuzzle import SuperDailyPuzzle
from utils.tree import Tree

# advent of code 2019 day 6
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = self.data.splitlines()
        raw_data = [line.rstrip() for line in lines]

        # convert raw map data to dictionary for easy orbit indexing
        orbits = {line.split(")")[0]: [] for line in raw_data}
        for line in raw_data:
            orbits[line.split(")")[0]].append(line.split(")")[1])

        # store universal orbital map as tree in parsed
        self.parsed = Tree()
        self.parsed.add_child("COM")

        # parse raw map data to tree (non-recursively)
        nodes = [self.parsed]
        while nodes:
            for child in nodes[0].children:
                if child in orbits.keys():
                    for orbit in orbits[child]:
                        nodes[0].children[child].add_child(orbit)
                    nodes.append(nodes[0].children[child])
            nodes.pop(0)

    def part_one(self):
        # universal_orbit_map.print_tree()
        self.part_one_result = self.parsed.children["COM"].checksum()

    def part_two(self):
        # find me (YOU) and santa (SAN)
        you = self.parsed.search_node("YOU")[2:]
        san = self.parsed.search_node("SAN")[2:]

        # determine common orbits
        both = [item for item in you if item in san]

        # distance is given by our distance w.r.t. COM minus twice the distance of smallest common orbit w.r.t. COM
        self.part_two_result = (len(you) - 1) + (len(san) - 1) - 2 * len(both)