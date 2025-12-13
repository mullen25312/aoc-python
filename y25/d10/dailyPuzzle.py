from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import product
import numpy as np

from scipy.optimize import LinearConstraint, milp

# advent of code 2025 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lights = []
        buttons = []
        joltages = []
        buttons_alt = []

        for line in self.data.splitlines():
            lights.append([0 if char == '.' else 1 for char in line.split(']')[0][1:]])
            buttons_alt.append([[int(slot) for slot in button[1:-1].split(",")] for button in line.split(']')[1][1:].split("{")[0][:-1].split(' ')])
            joltages.append([int(joltage) for joltage in line.split('{')[-1][:-1].split(',')])
        
        buttons = []
        for idx, butts in enumerate(buttons_alt):
            btns = []
            for but in butts:
                    tmp = [0]*len(lights[idx])
                    for light in but:
                        tmp[light] = 1
                    btns.append(tmp)
            buttons.append(btns)

        self.parsed = lights, buttons, joltages

        
    def part_one(self):
        lights, buttons, joltages = self.parsed

        final = 0
        for idx, buts in enumerate(buttons):
            res = {}
            combinations = list(product(range(2), repeat=len(buts)))
            for combination in combinations:
                tmp = [0]*len(lights[idx])
                
                for idx2, but in enumerate(buts): 
                    if combination[idx2] == 1: tmp = [a ^ b for a, b in zip(tmp, but)]
                res[combination] = tmp

            tmp_dict = {k: v for k, v in res.items() if v == lights[idx]}
            test = sorted(tmp_dict.items(), key=lambda item: sum(item[0]), reverse=False)
            final += sum(test[0][0])
        self.part_one_result = final

    def part_two(self): 
        _, buttons, joltages = self.parsed

        # lazy solution using milp from scipy
        res = 0
        for buts, joltage in zip(buttons, joltages):
            A = np.array(buts).T
            b = np.array(joltage)

            c = np.ones(A.shape[1])  # minimize the sum of button presses
            constraints = LinearConstraint(A, b, b)
            integrality = np.ones_like(c)  # all variables are integers
        
            sol = milp(c, constraints=constraints, integrality=integrality)
            res += int(sum(sol.x))

        self.part_two_result = res