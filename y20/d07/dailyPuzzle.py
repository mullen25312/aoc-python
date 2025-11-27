from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 7
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = {}
        
        for line in self.data.splitlines():
            container = line.split("contain")[0][:-5]
            content = line.split("contain")[1].split(",")
            content[-1] = content[-1][:-1]
            content_list = []
            for bag in content:
                bag = bag[1:]
                if bag == "no other bags":
                    content_list.append("no other bags")
                else:
                    amount = bag[0]
                    if int(amount) == 1:
                        content_list.append([int(amount), bag[2:-4]])
                    else:
                        content_list.append([int(amount), bag[2:-5]])

            self.parsed[container] = content_list

    def part_one(self):
        for rule in self.parsed:
            tmp = rule
            # while tmp in dict.keys():
        self.part_one_result = ""

    def part_two(self):
        self.part_two_result = ""