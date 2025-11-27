from utils.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2020 day 5
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        
        for line in self.data.splitlines():
            row = 0
            for idx, letter in enumerate(reversed(line[0:7])):
                if letter == "B":
                    row += 2 ** idx

            col = 0
            for idx, letter in enumerate(reversed(line[7:])):
                if letter == "R":
                    col += 2 ** idx

            self.parsed.append({"row": row, "col": col})

    def part_one(self):
        seat_ids = list(map(lambda seat: seat["row"] * 8 + seat["col"], self.parsed))
        self.part_one_result = max(seat_ids)

    def part_two(self):
        seat_ids = list(map(lambda seat: seat["row"] * 8 + seat["col"], self.parsed))
        seat_ids.sort()

        my_seat = None
        for idx in range(1, len(seat_ids)):
            if seat_ids[idx] - seat_ids[idx - 1] == 2:
                my_seat = seat_ids[idx] - 1

        self.part_two_result = my_seat