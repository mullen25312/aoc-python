from utils.superDailyPuzzle import SuperDailyPuzzle

def hash_string(string):
    current_value = 0
    for char in list(string):
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

# advent of code 2023 day 15
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = self.data.splitlines()[0].split(",")

    def part_one(self):
        self.part_one_result = sum([hash_string(string) for string in self.parsed])

    def part_two(self):
        
        boxes = {}
        for string in self.parsed:
            label = string.replace("-","=").split("=")[0]
            hash = hash_string(label)

            # box entry assignements
            if "=" in string:
                value = int(string.split("=")[1])

                # if box does not exist, add box and add entry
                if hash not in boxes.keys(): 
                    boxes[hash] = []
                    boxes[hash].append([label, value])
                # if box exists, check if entry exists and update, otherwise add entry
                else:
                    idx = [idx for (idx, item) in enumerate(boxes[hash]) if item[0] == label]
                    if len(idx) > 0: boxes[hash][idx[0]][1] = value
                    else: boxes[hash].append([label, value])

            # box entry deletions
            if "-" in string:
                # if box exists somethin might be deleted
                if hash in boxes.keys():
                    # if entry exists delete it
                    idx = [idx for (idx, item) in enumerate(boxes[hash]) if item[0] == label]
                    if len(idx) > 0: boxes[hash].pop(idx[0])

        self.part_two_result = sum([sum([(k+1) * (idx+1) * item[1] for (idx, item) in enumerate(v)]) for k, v in boxes.items()])