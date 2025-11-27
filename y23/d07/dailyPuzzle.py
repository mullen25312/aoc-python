from utils.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict 

card_strength = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
card_strength2 = {"A":14, "K":13, "Q":12,        "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2, "J":1}

def rating(hand):
    config_score = sum([card_strength[label]*(100**(5-idx-1)) for (idx, label) in enumerate(hand)])

    hand_dict = defaultdict(lambda: 0)
    for label in hand: hand_dict[label] += 1

    tmp = sorted(hand_dict.values(), reverse=True)

    if tmp[0] == 5: return 7*100**5 + config_score
    elif tmp[0] == 4: return 6*100**5 + config_score
    elif tmp[0] == 3 and tmp[1] == 2: return 5*100**5 + config_score
    elif tmp[0] == 3: return 4*100**5 + config_score
    elif tmp[0] == 2 and tmp[1] == 2: return 3*100**5 + config_score
    elif tmp[0] == 2: return 2*100**5 + config_score
    else: return 1*100**5 + config_score

def rating2(hand):
    config_score = sum([card_strength2[label]*(100**(5-idx-1)) for (idx, label) in enumerate(hand)])

    hand_dict = defaultdict(lambda: 0)
    for label in hand: hand_dict[label] += 1

    jokers = hand_dict["J"]
    hand_dict["J"] = 0
    tmp = sorted(hand_dict.values(), reverse=True)
    
    if jokers == 5: return 7*100**5 + config_score
    elif jokers == 4:
        return 7*100**5 + config_score
    elif jokers == 3:
        if tmp[0] == 2: return 7*100**5 + config_score
        else: return 6*100**5 + config_score
    elif jokers == 2:
        if tmp[0] == 3: return 7*100**5 + config_score
        elif tmp[0] == 2: return 6*100**5 + config_score
        else: return 4*100**5 + config_score
    elif jokers == 1:
        if tmp[0] == 4: return 7*100**5 + config_score
        elif tmp[0] == 3: return 6*100**5 + config_score
        elif tmp[0] == 2 and tmp[1] == 2 : return 5*100**5 + config_score
        elif tmp[0] == 2: return 4*100**5 + config_score
        elif tmp[0] == 2: return 3*100**5 + config_score
        else: return 2*100**5 + config_score
    if jokers == 0:
        if tmp[0] == 5: return 7*100**5 + config_score
        elif tmp[0] == 4: return 6*100**5 + config_score
        elif tmp[0] == 3 and tmp[1] == 2 : return 5*100**5 + config_score
        elif tmp[0] == 3: return 4*100**5 + config_score
        elif tmp[0] == 2 and tmp[1] == 2: return 3*100**5 + config_score
        elif tmp[0] == 2: return 2*100**5 + config_score
        else: return 1*100**5 + config_score

# advent of code 2023 day 7
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        tmp = self.data.splitlines()

        hands, bids = [], []
        for line in tmp:
            hands.append(line.split(" ")[0])
            bids.append(int(line.split(" ")[1]))

        self.parsed = list(zip(hands, bids))

    def part_one(self):

        self.parsed.sort(key = lambda x: rating(x[0]))
        self.part_one_result = sum([hand[1]*(idx+1) for (idx, hand) in enumerate(self.parsed)])

    def part_two(self):

        self.parsed.sort(key = lambda x: rating2(x[0]))
        self.part_two_result = sum([hand[1]*(idx+1) for (idx, hand) in enumerate(self.parsed)])