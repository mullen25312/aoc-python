class DailyPuzzle16:
    def __init__(self):
        self.ranges = {}
        self.mTicket = []
        self.tickets = []
        self.valid = []

    def read_data(self):
        with open("./d16/input.txt") as f:
            state = 0
            for line in f:
                if line == '\n':
                    continue
                elif line.strip() == 'your ticket:':
                    state  = 1
                elif line.strip() == 'nearby tickets:':
                    state = 2
                elif state == 0:
                    field = line.split(':')[0].strip()
                    tmp1 = line.split(':')[1].split('or')[0].strip()
                    tmp2 = line.split(':')[1].split('or')[1].strip()
                    self.ranges[field] = [tmp1, tmp2]
                elif state == 1:
                    self.mTicket = [int(n) for n in line.strip().split(',')]
                else:
                    self.tickets.append([int(n) for n in line.strip().split(',')])

    def solve_part_one(self):
        invalid_fields = []
        for ticket in self.tickets:
            for num in ticket:
                invalid = 0
                for ran in self.ranges.values():
                    tmp0 = [int(n) for n in ran[0].split('-')]
                    tmp1 = [int(n) for n in ran[1].split('-')]

                    if (tmp0[0] <= num <= tmp0[1]) or (tmp1[0] <= num <= tmp1[1]):
                        break
                    else:
                        invalid += 1
                if invalid == len(self.ranges.values()):
                    invalid_fields.append(num)

        return sum(invalid_fields)

    def solve_part_two(self):
        print('test')