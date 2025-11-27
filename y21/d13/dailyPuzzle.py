from utils.superDailyPuzzle import SuperDailyPuzzle


def fold_action(paper, fold):
    if fold[0] == "x":
        for point in paper.copy():
            if point[0] >= fold[1]:
                paper.add((fold[1] - (point[0] - fold[1]), point[1]))
                paper.remove(point)
    elif fold[0] == "y":
        for point in paper.copy():
            if point[1] >= fold[1]:
                paper.add((point[0], fold[1] - (point[1] - fold[1])))
                paper.remove(point)
    return paper


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = {"paper": None, "folds": None}

        tmp = self.data.split("\n\n")
        self.parsed["paper"] = set(tuple(int(number) for number in line.split(",")) for line in tmp[0].splitlines())
        self.parsed["folds"] = [(line.split("=")[0][-1], int(line.split("=")[1])) for line in tmp[1].splitlines()]

    def part_one(self):
        # fold once
        self.part_one_result = len(fold_action(self.parsed["paper"], self.parsed["folds"][0]))

    def part_two(self):
        # fold multiple times
        paper = self.parsed["paper"]
        for idx in range(len(self.parsed["folds"])):
            paper = fold_action(paper, self.parsed["folds"][idx])

        # visualize
        output = ""
        for y in range(max([point[1] for point in paper]) + 1):
            for x in range(max([point[0] for point in paper]) + 1):
                output += "#" if (x, y) in paper else "."
            output += "\n"
        # print(output)

        self.part_two_result = "FAGURZHE"
