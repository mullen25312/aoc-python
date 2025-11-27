from utils.superDailyPuzzle import SuperDailyPuzzle

# from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from itertools import combinations

@dataclass
class Cuboid:
    def __init__(self, x=(0, 0), y=(0, 0), z=(0, 0)):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def volume(self):
        return (self.x[1] - self.x[0] + 1) * (self.y[1] - self.y[0] + 1) * (self.z[1] - self.z[0] + 1)


def check_overlap(first: Cuboid, second: Cuboid) -> bool:
    if (
        (tuple(sorted((*first.x, *second.x))) == (*first.x, *second.x) or tuple(sorted((*first.x, *second.x))) == (*second.x, *first.x))
        or (tuple(sorted((*first.y, *second.y))) == (*first.y, *second.y) or tuple(sorted((*first.y, *second.y))) == (*second.y, *first.y))
        or (tuple(sorted((*first.z, *second.z))) == (*first.z, *second.z) or tuple(sorted((*first.z, *second.z))) == (*second.z, *first.z))
    ):
        return False
    else:
        return True


def add_cuboids(first: Cuboid, second: Cuboid) -> set:
    tmp_x = sorted((first.x[0], first.x[1], second.x[0], second.x[1]))
    tmp_y = sorted((first.y[0], first.y[1], second.y[0], second.y[1]))
    tmp_z = sorted((first.z[0], first.z[1], second.z[0], second.z[1]))

    # tmp_xx = tuple(zip(tmp_x, tmp_x[1:]))
    # tmp_yy = tuple(zip(tmp_y, tmp_y[1:]))
    # tmp_zz = tuple(zip(tmp_z, tmp_z[1:]))

    tmp_xx = ((tmp_x[0], tmp_x[1]), (tmp_x[1], tmp_x[2]), (tmp_x[2], tmp_x[3]))
    tmp_yy = ((tmp_y[0], tmp_y[1]), (tmp_y[1], tmp_y[2]), (tmp_y[2], tmp_y[3]))
    tmp_zz = ((tmp_z[0], tmp_z[1]), (tmp_z[1], tmp_z[2]), (tmp_z[2]+1, tmp_z[3]))

    cuboids = product(tmp_xx, tmp_yy, tmp_zz)

    res = set()
    for cube in cuboids:
        tmp = Cuboid(x=(cube[0][0], cube[0][1]), y=(cube[1][0], cube[1][1]), z=(cube[2][0], cube[2][1]))
        if check_overlap(first, tmp) or check_overlap(second, tmp):
            res.add(tmp)
    return res


def sub_cuboids(first: Cuboid, second: Cuboid) -> set:
    tmp_x = sorted((*first.x, *second.x))
    tmp_y = sorted((*first.y, *second.y))
    tmp_z = sorted((*first.z, *second.z))

    tmp_x = tuple(zip(tmp_x, tmp_x[1:]))
    tmp_y = tuple(zip(tmp_y, tmp_y[1:]))
    tmp_z = tuple(zip(tmp_z, tmp_z[1:]))

    cuboids = product(tmp_x, tmp_y, tmp_z)

    res = set()
    for cube in cuboids:
        tmp = Cuboid(cube[0], cube[1], cube[2])
        if check_overlap(first, tmp):
            res.add(tmp)
    return res


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = []
        for line in self.data.splitlines():
            state = line.split(" ")[0]
            x = tuple(int(number) for number in line.split("=")[1].split(",")[0].split(".."))
            y = tuple(int(number) for number in line.split("=")[2].split(",")[0].split(".."))
            z = tuple(int(number) for number in line.split("=")[3].split(",")[0].split(".."))
            self.parsed.append([state, ((x[0], x[1]), (y[0], y[1]), (z[0], z[1]))])

    def part_one(self):
        reactor = dict()

        for step in self.parsed:
            x_range = (max(-50, step[1][0][0]), min(step[1][0][1] + 1, 51))
            y_range = (max(-50, step[1][1][0]), min(step[1][1][1] + 1, 51))
            z_range = (max(-50, step[1][2][0]), min(step[1][2][1] + 1, 51))
            for i, j, k in product(range(*x_range), range(*y_range), range(*z_range)):

                if step[0] == "on":
                    reactor[(i, j, k)] = True
                else:
                    if (i, j, k) in reactor.keys():
                        reactor.pop((i, j, k))

        self.part_one_result = len(reactor)

    def part_two(self):
        # memory issue with the above solution --> other representation needed
        res = set()
        res.add(Cuboid(x=self.parsed[0][1][0], y=self.parsed[0][1][1], z=self.parsed[0][1][2]))

        # for step in self.parsed[1:]:
        #     tmp = Cuboid(x=step[1][0], y=step[1][1], z=step[1][2])
        #     res_new = set()
        #     for cube in res:
        #         if step[0] == "on":
        #             res_new.update(add_cuboids(cube, tmp))
        #         else:
        #             res_new.update(sub_cuboids(cube, tmp))
        #     res = res_new

        first = Cuboid(x=(0,2), y=(0,2), z=(0,2))
        second = Cuboid(x=(0,2), y=(0,2), z=(0,3))
        # second = Cuboid(x=(10,12), y=(10,12), z=(11,13))
        tmp = add_cuboids(first, second)
        # print(sum([cuboid.volume() for cuboid in tmp]))
        
        # print('test')

        self.part_two_result = sum([cuboid.volume() for cuboid in res])
