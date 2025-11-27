from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2019 day 3
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = self.data.strip().split('\n')
        self.line1 = lines[0].split(",")
        self.line2 = lines[1].split(",")

    def part_one(self):
        # create list of positions of line1
        line1Positions = set()
        pos = [0, 0]
        for move in enumerate(self.line1):
            direction = move[1][0]
            distance = int(move[1][1:])

            if direction == "R":  # moved to the right
                for step in range(1, distance + 1):
                    line1Positions.add((pos[0] + step, pos[1]))
                pos[0] += distance

            if direction == "L":  # moved to the left
                for step in range(1, distance + 1):
                    line1Positions.add((pos[0] - step, pos[1]))
                pos[0] -= distance

            if direction == "U":  # moved up
                for step in range(1, distance + 1):
                    line1Positions.add((pos[0], pos[1] + step))
                pos[1] += distance

            if direction == "D":  # moved down
                for step in range(1, distance + 1):
                    line1Positions.add((pos[0], pos[1] - step))
                pos[1] -= distance

        # create list of positions of line2
        line2Positions = set()
        pos = [0, 0]
        for move in enumerate(self.line2):
            direction = move[1][0]
            distance = int(move[1][1:])

            if direction == "R":  # moved to the right
                for step in range(1, distance + 1):
                    line2Positions.add((pos[0] + step, pos[1]))
                pos[0] += distance

            if direction == "L":  # moved to the left
                for step in range(1, distance + 1):
                    line2Positions.add((pos[0] - step, pos[1]))
                pos[0] -= distance

            if direction == "U":  # moved up
                for step in range(1, distance + 1):
                    line2Positions.add((pos[0], pos[1] + step))
                pos[1] += distance

            if direction == "D":  # moved down
                for step in range(1, distance + 1):
                    line2Positions.add((pos[0], pos[1] - step))
                pos[1] -= distance

        crossings = line1Positions.intersection(line2Positions)
        distances = [abs(point[0]) + abs(point[1]) for point in list(crossings)]
        self.part_one_result = min(distances)

    def part_two(self):
        # create list of positions of line1
        line1Positions = dict()
        pos = [0, 0]
        stepsTaken = 0
        for move in enumerate(self.line1):
            direction = move[1][0]
            distance = int(move[1][1:])
            if direction == "R":  # moved to the right
                for step in range(1, distance + 1):
                    line1Positions[(pos[0] + step, pos[1])] = stepsTaken + step
                pos[0] += distance

            if direction == "L":  # moved to the left
                for step in range(1, distance + 1):
                    line1Positions[(pos[0] - step, pos[1])] = stepsTaken + step
                pos[0] -= distance

            if direction == "U":  # moved up
                for step in range(1, distance + 1):
                    line1Positions[(pos[0], pos[1] + step)] = stepsTaken + step
                pos[1] += distance

            if direction == "D":  # moved down
                for step in range(1, distance + 1):
                    line1Positions[(pos[0], pos[1] - step)] = stepsTaken + step
                pos[1] -= distance
            stepsTaken += distance

        # create list of positions of line2
        line2Positions = dict()
        pos = [0, 0]
        stepsTaken = 0
        for move in enumerate(self.line2):
            direction = move[1][0]
            distance = int(move[1][1:])
            if direction == "R":  # moved to the right
                for step in range(1, distance + 1):
                    line2Positions[(pos[0] + step, pos[1])] = stepsTaken + step
                pos[0] += distance

            if direction == "L":  # moved to the left
                for step in range(1, distance + 1):
                    line2Positions[(pos[0] - step, pos[1])] = stepsTaken + step
                pos[0] -= distance

            if direction == "U":  # moved up
                for step in range(1, distance + 1):
                    line2Positions[(pos[0], pos[1] + step)] = stepsTaken + step
                pos[1] += distance

            if direction == "D":  # moved down
                for step in range(1, distance + 1):
                    line2Positions[(pos[0], pos[1] - step)] = stepsTaken + step
                pos[1] -= distance
            stepsTaken += distance

        intersections = set(line1Positions.keys()).intersection(
            set(line2Positions.keys())
        )

        intersectionSteps = []
        for intersection in intersections:
            intersectionSteps.append(
                line1Positions[intersection] + line2Positions[intersection]
            )
        self.part_two_result = min(intersectionSteps)