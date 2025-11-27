from utils.superDailyPuzzle import SuperDailyPuzzle
import copy

# advent of code 2022 day 21
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]

        # parse monkeys
        self.parsed = dict()
        for line in lines:
            monkey, yell = line.split(": ")
            if len(yell.split(" ")) == 3:
                operand1, operator, operand2 = yell.split(" ")
                self.parsed[monkey] = {"operand1":operand1, "operand2": operand2, "operator": operator}
            else:
                 self.parsed[monkey] = {"result":int(yell)}

        # for monkey in self.parsed:
        #     print(str(monkey) + ": " + str(self.parsed[monkey]))

    def part_one(self):
        monkeys = copy.deepcopy(self.parsed)

        finished = False
        while not finished:
            finished = True
            for monkey in monkeys:
                if "result" in monkeys[monkey].keys():
                    pass
                else:
                    operand1 = monkeys[monkey]["operand1"]
                    operand2 = monkeys[monkey]["operand2"]
                    operator = monkeys[monkey]["operator"]
                    if "result" in monkeys[operand1].keys() and "result" in monkeys[operand2].keys():
                        if operator == '+': monkeys[monkey]["result"] = monkeys[operand1]["result"] + monkeys[operand2]["result"] 
                        if operator == '-': monkeys[monkey]["result"] = monkeys[operand1]["result"] - monkeys[operand2]["result"] 
                        if operator == '*': monkeys[monkey]["result"] = monkeys[operand1]["result"] * monkeys[operand2]["result"] 
                        if operator == '/': monkeys[monkey]["result"] = monkeys[operand1]["result"] // monkeys[operand2]["result"] 
                    else:
                        finished = False
        
        # for monkey in monkeys:
        #     print(str(monkey) + ": " + str(monkeys[monkey]))

        self.part_one_result = monkeys["root"]["result"]

    def part_two(self):
        self.part_two_result = 0
