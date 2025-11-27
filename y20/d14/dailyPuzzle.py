from utils.superDailyPuzzle import SuperDailyPuzzle
import itertools


# advent of code 2020 day 14
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = [line for line in self.data.splitlines()]

    def part_one(self):
        mem = {}
        mask_ones = 2 ** 36
        mask_zeros = 0
        for instruction in self.parsed:
            com = instruction.split("=")[0].strip()
            arg = instruction.split("=")[1].strip()

            if com == "mask":
                mask_ones = int("".join(["1" if bit == "1" else "0" for bit in arg]), 2)  # for or
                mask_zeros = int("".join(["0" if bit == "0" else "1" for bit in arg]), 2)  # for and

            else:
                mem[int(com[4:-1])] = (int(arg) | mask_ones) & mask_zeros

        self.part_one_result = sum(mem.values())

    def part_two(self):
        mem = {}
        for instruction in self.parsed:
            com = instruction.split("=")[0].strip()
            arg = instruction.split("=")[1].strip()
            if com == "mask":
                tmp = [["0", "1"] if (c == "X") else c for c in arg]
                combs = ["".join(lst) for lst in list(itertools.product(*tmp))]
                mask_ones = "".join(["1" if bit == "1" else "0" for bit in arg])
                mask_xses = "".join(["0" if bit == "X" else "1" for bit in arg])
            else:
                base_address = (int(com[4:-1]) | int(mask_ones, 2)) & int(mask_xses, 2)
                for comb in combs:
                    mem[base_address | int(comb, 2)] = int(arg)
        self.part_two_result = sum(mem.values())