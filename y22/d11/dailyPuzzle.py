from utils.superDailyPuzzle import SuperDailyPuzzle
import copy

def gcd(a, b):
    if a == 0:
        return b
    # recursively calculating the gcd.
    return gcd(b % a, a)

def lcm(arg):
    res = 1
    for idx in arg:
        res = res*idx//gcd(res, idx)
    return res

class Monkey():
    def __init__(self, items , operation, divisor, next_true_monkey, next_false_monkey):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.next_true_monkey = next_true_monkey
        self.next_false_monkey = next_false_monkey
        self.inspection_counter = 0

    def inspect1(self):
        result = []
        while self.items:
            tmp = self.items.pop(0)
            tmp = self.operation(tmp)
            tmp = tmp // 3
            result.append((tmp, self.next_false_monkey)) if tmp % self.divisor else result.append((tmp, self.next_true_monkey))
            self.inspection_counter += 1
        return result

    def inspect2(self, lcm):
        result = []
        while self.items:
            tmp = self.items.pop(0)
            tmp = self.operation(tmp)
            tmp = tmp % lcm
            result.append((tmp, self.next_false_monkey)) if tmp % self.divisor else result.append((tmp, self.next_true_monkey))
            self.inspection_counter += 1
        return result
                
# advent of code 2022 day 11
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read and parse input data
        lines = [line.strip() for line in self.data.splitlines()]
        self.parsed = []

        if len(lines) == 27: # a bit hacky, but I really do not wanna parse the input
            # demo
            monkey0 = Monkey([79, 98], lambda x: x*19, 23, 2, 3); self.parsed.append(monkey0)
            monkey1 = Monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0); self.parsed.append(monkey1)
            monkey2 = Monkey([79, 60, 97], lambda x: x*x, 13, 1, 3); self.parsed.append(monkey2)
            monkey3 = Monkey([74], lambda x: x+3, 17, 0, 1); self.parsed.append(monkey3)
        else:
            # input 
            monkey0 = Monkey([66, 71, 94], lambda x: x*5, 3, 7, 4); self.parsed.append(monkey0)
            monkey1 = Monkey([70], lambda x: x+6, 17, 3, 0); self.parsed.append(monkey1)
            monkey2 = Monkey([62, 68, 56, 65, 94, 78], lambda x: x+5, 2, 3, 1); self.parsed.append(monkey2)
            monkey3 = Monkey([89, 94, 94, 67], lambda x: x+2, 19, 7, 0); self.parsed.append(monkey3)
            monkey4 = Monkey([71, 61, 73, 65, 98, 98, 63], lambda x: x*7, 11, 5, 6); self.parsed.append(monkey4)
            monkey5 = Monkey([55, 62, 68, 61, 60], lambda x: x+7, 5, 2, 1); self.parsed.append(monkey5)
            monkey6 = Monkey([93, 91, 69, 64, 72, 89, 50, 71], lambda x: x+1, 13, 5, 2); self.parsed.append(monkey6)
            monkey7 = Monkey([76, 50], lambda x: x*x, 7, 4, 6); self.parsed.append(monkey7)

    def part_one(self):
        monkeys = copy.deepcopy(self.parsed)

        for idx in range(0, 20):
            for monkey in monkeys:
                for (item, next_monkey) in monkey.inspect1():
                    monkeys[next_monkey].items.append(item)

        monkeys = sorted(monkeys, key=lambda x: -x.inspection_counter)     
        self.part_one_result = monkeys[0].inspection_counter * monkeys[1].inspection_counter 

    def part_two(self):
        monkeys = copy.deepcopy(self.parsed)
        least_common_multiplier = lcm([monkey.divisor for monkey in monkeys])

        for idx in range(0, 10000):
            for monkey in monkeys:
                for (item, next_monkey) in monkey.inspect2(least_common_multiplier):
                    monkeys[next_monkey].items.append(item)
        
        monkeys = sorted(monkeys, key=lambda x: -x.inspection_counter)   
        self.part_two_result = monkeys[0].inspection_counter * monkeys[1].inspection_counter 
