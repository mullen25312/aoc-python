from utils.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations
import numpy as np

def crossings_2d(pair):
    x0 = pair[0][0][0]; x1 = pair[1][0][0]; y0 = pair[0][0][1]; y1 = pair[1][0][1]
    vx0 = pair[0][1][0]; vx1 = pair[1][1][0]; vy0 = pair[0][1][1]; vy1 = pair[1][1][1]
    if (vy1*vx0- vy0*vx1) == 0: return (0, 0, 0, 0)
    else:
        t1 =(vy0*(x1-x0) - vx0*(y1-y0)) / (vx0*vy1- vy0*vx1)
        t0 = ((x1-x0) + vx1*t1)/vx0
        xs = x0+vx0*t0; ys = y0+vy0*t0
        return (t0, t1, xs, ys)
    
    # b = np.mat([[pair[1][0][0]-pair[0][0][0]], [pair[1][0][1]-pair[0][0][1]]])
    # A = np.mat([[pair[0][1][0], -pair[1][1][0]], [pair[0][1][1], -pair[1][1][1]]])
    # if np.linalg.det(A) == 0: return (0, 0, 0, 0)
    # else:
    #     t = np.linalg.solve(A,b) # t = np.linalg.inv(A)*b
    #     xs = np.mat(pair[0][0][0:2]).transpose() + np.mat(pair[0][1][0:2]).transpose() * t[0]
    #     return (t[0], t[1], xs[0], xs[1])

def check_task2(traj):
    v = traj[1]
    vs = [-3, 1, 2]
    tmp = np.cross(v, vs)
    # print(tmp)
    # print(np.cross(tmp, vs))

# advent of code 2023 day 24
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        trajs = []
        for line in self.data.splitlines():
            pos = [int(x.strip()) for x in line.split("@")[0].split(",")]
            vel = [int(x.strip()) for x in line.split("@")[1].split(",")]
            trajs.append([pos,vel])

        self.parsed = trajs

    def part_one(self):
        trajs = self.parsed

        if len(trajs) == 5: l = 7; r=27 
        else: l = 200000000000000; r = 400000000000000

        self.part_one_result = sum([1 for (t0, t1, x, y) in map(crossings_2d, combinations(trajs, 2)) if l<=x<=r and l<=y<=r and t0>0 and t1>0])

    def part_two(self):
        trajs = self.parsed

        for traj in trajs:
            check_task2(traj)
        self.part_two_result = 0
