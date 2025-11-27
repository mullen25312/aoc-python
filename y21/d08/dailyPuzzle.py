from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import product


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = {"samples": [], "output": []}
        self.parsed["samples"] = [[digit for digit in line.split("|")[0].split(" ")][:-1] for line in self.data.splitlines()]
        self.parsed["outputs"] = [[digit for digit in line.split("|")[1].split(" ")][1:] for line in self.data.splitlines()]

    def part_one(self):
        result = 0
        for outputs in self.parsed["outputs"]:
            result += sum([((len(output) == 2) or (len(output) == 3) or (len(output) == 4) or (len(output) == 7)) for output in outputs])
        self.part_one_result = result

    def part_two(self):
        segments = ["a", "b", "c", "d", "e", "f", "g"]  # all possible segments
        pattern2digits = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}  # segment patterns to digits

        # for every display
        result = 0
        for idx, sample in enumerate(self.parsed["samples"]):

            # build histogram
            hist = {segment: "".join(sample).count(segment) for segment in segments}

            # segment deduction according to careful analysis
            seg2seg = {}
            seg2seg["e"] = [segment for segment in hist if (hist[segment] == 4)][0]  # only e has count 4 for all ten digit patterns
            seg2seg["b"] = [segment for segment in hist if (hist[segment] == 6)][0]  # only b has count 6 for all ten digit patterns
            seg2seg["f"] = [segment for segment in hist if (hist[segment] == 9)][0]  # only f has count 9 for all ten digit patterns

            seg2seg["c"] = [pattern for pattern in sample if (len(pattern) == 2)][0].replace(seg2seg["f"], "")  # only number 1 has two segments minus f is c
            seg2seg["a"] = [pattern for pattern in sample if (len(pattern) == 3)][0].replace(seg2seg["f"], "").replace(seg2seg["c"], "")  # only number 7 has three segments minus f minus c is a
            seg2seg["d"] = [pattern for pattern in sample if (len(pattern) == 4)][0].replace(seg2seg["f"], "").replace(seg2seg["c"], "").replace(seg2seg["b"], "")  # only number 4 has four segments minus f minus c minus b is d
            seg2seg["g"] = "".join(segments).replace(seg2seg["a"], "").replace(seg2seg["b"], "").replace(seg2seg["c"], "").replace(seg2seg["d"], "").replace(seg2seg["e"], "").replace(seg2seg["f"], "")  # last one left is g

            # invert translation
            inv_seg2seg = {y: x for x, y in seg2seg.items()}

            # translate output pattern
            trans_output_pattern = []
            for output_pattern in self.parsed["outputs"][idx]:
                trans_output_pattern.append("".join(sorted([inv_seg2seg[segment] for segment in output_pattern])))

            # convert output pattern to integer and sum over all outputs
            result += sum([pattern2digits[pattern] * 10 ** idx for idx, pattern in enumerate(reversed(trans_output_pattern))])

        self.part_two_result = result
