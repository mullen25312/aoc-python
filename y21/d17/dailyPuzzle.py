from utils.superDailyPuzzle import SuperDailyPuzzle


def simulate(vel, target_area):
    pos = [0, 0]
    sol = [pos.copy()]

    while not ((target_area["x"][0] <= pos[0] <= target_area["x"][1]) and (target_area["y"][0] <= pos[1] <= target_area["y"][1])):
        pos[0] += vel[0]
        pos[1] += vel[1]
        vel[0] += (vel[0] < 0) - (vel[0] > 0)
        vel[1] -= 1
        sol.append(pos.copy())

        if pos[0] > target_area["x"][1] or pos[1] < target_area["y"][0]:
            return False

    return sol


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input

        tmp = self.data.splitlines()[0].split(": ")[1].split(",")
        self.parsed = {"x": tuple(int(number) for number in tmp[0].split("=")[1].split("..")), "y": tuple(int(number) for number in tmp[1].split("=")[1].split(".."))}

    def part_one(self):
        sols = dict()
        vel_min = (0, 0)
        vel_max = (50, 150)

        for velx in range(vel_min[0], vel_max[0]):
            for vely in range(vel_min[1], vel_max[1]):
                vel = (velx, vely)
                sol = simulate(list(vel), self.parsed)
                if sol:
                    sols[vel] = sol

        self.part_one_result = max([max(sols[sol], key=lambda x: x[1])[1] for sol in sols])

    def part_two(self):
        sols = dict()
        vel_min = (0, self.parsed["y"][0])
        vel_max = (self.parsed["x"][1] * 5 // 4, 250)

        for velx in range(vel_min[0], vel_max[0]):
            for vely in range(vel_min[1], vel_max[1]):
                vel = (velx, vely)
                sol = simulate(list(vel), self.parsed)
                if sol:
                    sols[vel] = sol

        self.part_two_result = len(sols)
