from utils.superDailyPuzzle import SuperDailyPuzzle


# advent of code 2020 day 16
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.ranges = {}
        self.mTicket = []
        self.tickets = []
        self.valid = []
        
        lines = self.data.strip().split('\n')
        state = 0
        for line in lines:
            if line == '':
                continue
            elif line.strip() == 'your ticket:':
                state = 1
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

    def part_one(self):
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

        self.part_one_result = sum(invalid_fields)

    def part_two(self):
        self.part_two_result = 0