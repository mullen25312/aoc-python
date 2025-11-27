from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations
from utils.tree import Tree


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # self.parsed = [bin(int(line, 2)) for line in self.data.splitlines()]
        self.parsed = [line for line in self.data.splitlines()]
        # print(self.parsed)

    def part_one(self):
        result = ""
        result_not = ""
        for idx in range(len(self.parsed[0])):
            tmp = 0
            for bitstring in self.parsed:
                tmp += int(bitstring[idx])
            # result.append(tmp)
            if tmp > len(self.parsed) // 2:
                result += "1"
                result_not += "0"
            else:
                result += "0"
                result_not += "1"

        result = int(result, 2)
        result_not = int(result_not, 2)
        # result_not = ~result & 0b0000_0000_0001_1111
        # result_not = ~result & 0b0000_1111_1111_1111

        self.part_one_result = result * result_not

    def part_two(self):

        bitTree = Tree()

        for bitstring in self.parsed:
            parent = bitTree
            for bit in bitstring:
                if bit not in parent.children:
                    parent.add_child(bit)
                parent = parent.children[bit]

        # bitTree.print_tree()

        # find oxygen generator rating
        parent = bitTree
        result = ""
        while parent.children:
            if "0" not in parent.children:
                parent = parent.children["1"]
                result += "1"
                continue

            if "1" not in parent.children:
                parent = parent.children["0"]
                result += "0"
                continue

            if parent.children["0"].number_of_leaves() > parent.children["1"].number_of_leaves():
                parent = parent.children["0"]
                result += "0"
            else:
                parent = parent.children["1"]
                result += "1"

        oxy = int(result, 2)

        # find co2 scrubber rating
        parent = bitTree
        result = ""
        while parent.children:
            if "0" not in parent.children:
                parent = parent.children["1"]
                result += "1"
                continue

            if "1" not in parent.children:
                parent = parent.children["0"]
                result += "0"
                continue

            if parent.children["0"].number_of_leaves() <= parent.children["1"].number_of_leaves():
                parent = parent.children["0"]
                result += "0"
            else:
                parent = parent.children["1"]
                result += "1"

        co2 = int(result, 2)

        self.part_two_result = oxy * co2

