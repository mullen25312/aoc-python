from utils.superDailyPuzzle import SuperDailyPuzzle
import math
import re
import numpy as np
from itertools import combinations

# positions of each coordinate in full vector
coordinates = {"x": 0, "y": 1, "z": 2}

# regular expression for parsing input
reg_expr = r"([xyz])=(-?\d+)"

# least common multiple based on greates common divisor
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def moons_difference_equation(moons):
    # split given state into positions and velocities
    dim = moons.shape[1] // 2
    pos = moons.copy()[:, 0:dim]
    vel = moons.copy()[:, dim : 2 * dim]

    # apply gravity
    n = pos.shape[0]
    # for each combination
    for pair in combinations(range(0, n), 2):
        # if moons position is greather than others position add -1 (1) to velocity
        vel[pair[0], np.greater(pos[pair[0], :], pos[pair[1], :])] -= 1
        vel[pair[1], np.greater(pos[pair[0], :], pos[pair[1], :])] += 1

        # if moons position is lesser than others position add 1 (-1) to velocity
        vel[pair[0], np.less(pos[pair[0], :], pos[pair[1], :])] += 1
        vel[pair[1], np.less(pos[pair[0], :], pos[pair[1], :])] -= 1

    # add velocity to position
    pos += vel

    # return stacked vector as next state
    return np.concatenate((pos, vel), axis=1)

def total_energy(moons):
    # split into positions and velocities
    dim = moons.shape[1] // 2
    pos = moons.copy()[:, 0:dim]
    vel = moons.copy()[:, dim : 2 * dim]

    # compute energies
    potential_energies = np.sum(np.absolute(pos), axis=1)
    kinetic_energies = np.sum(np.absolute(vel), axis=1)
    energies = np.multiply(potential_energies, kinetic_energies)

    # return sum of energies
    return sum(energies)

# advent of code 2019 day 12
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read input data
        lines = self.data.splitlines()
        self.parsed = []
        for idx, line in enumerate(lines):
            results = re.findall(reg_expr, line)
            self.parsed.append([0 for result in 2 * results])
            for result in results:
                self.parsed[idx][coordinates[result[0]]] = int(result[1])

    def part_one(self):
        steps = 1000  # number of steps
        moons = [np.array(self.parsed)]  # initial state

        # evaluate difference equation steps times
        for _ in range(0, steps):
            moons.append(moons_difference_equation(moons[-1]))

        # return total energy of last state
        self.part_one_result = total_energy(moons[-1])

    def part_two(self):
        # each coordinate is independent of each other
        # therefore find each axis cycle number

        # simulate for x-axis
        cnt_x = 1
        moons = [np.array(self.parsed)[:, [0, 3]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_x += 1

        # simulate for y-axis
        cnt_y = 1
        moons = [np.array(self.parsed)[:, [1, 4]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_y += 1

        # simulate for z-axis
        cnt_z = 1
        moons = [np.array(self.parsed)[:, [2, 5]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_z += 1

        # overall cycle number is least common multiple of each axis cycle number
        self.part_two_result = lcm(lcm(cnt_x, cnt_y), cnt_z)