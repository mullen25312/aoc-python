from utils.superDailyPuzzle import SuperDailyPuzzle

def play_game(player0, player1):
    while len(player0) != 0 and len(player1) != 0:
        card0 = player0.pop(0)
        card1 = player1.pop(0)
        if card0 > card1:
            player0.append(card0)
            player0.append(card1)
        else:
            player1.append(card1)
            player1.append(card0) 

    winner = 0 if (len(player0) != 0) else 1
    return winner, player0, player1

def play_game_recursive(player0, player1):
    card_comb_played = set()
    while len(player0) != 0 and len(player1) != 0:
        if (tuple(player0), tuple(player1)) in card_comb_played:
            return 0, player0, player1
        else:
             card_comb_played.add((tuple(player0), tuple(player1)))
        card0 = player0.pop(0)
        card1 = player1.pop(0)
        if card0 > len(player0) or card1 > len(player1):
            if card0 > card1:
                player0.append(card0)
                player0.append(card1)
            else:
                player1.append(card1)
                player1.append(card0)
        else:
            winner, _, _ = play_game_recursive(list(player0[:card0]), list(player1[:card1]))
            if winner == 0:
                player0.append(card0)
                player0.append(card1)
            else:
                player1.append(card1)
                player1.append(card0)

    winner = 0 if (len(player0) != 0) else 1
    return winner, player0, player1


# advent of code 2020 day 22
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        self.parsed = []
        tmp = []
        
        for line in self.data.split('\n'):
            if line == '':
                if tmp:
                    self.parsed.append(tmp)
                    tmp = []
            elif line.strip().isdigit():
                tmp.append(int(line))

        if tmp:
            self.parsed.append(tmp)

    def part_one(self):
        player0 = list(self.parsed[0])
        player1 = list(self.parsed[1])

        winner, player0, player1 = play_game(player0, player1)
        if winner == 0:
            self.part_one_result = sum([val*(idx+1) for (idx, val) in enumerate(player0[::-1])])
        else:
            self.part_one_result = sum([val*(idx+1) for (idx, val) in enumerate(player1[::-1])])
        
    def part_two(self):
        player0 = list(self.parsed[0])
        player1 = list(self.parsed[1])

        winner, player0, player1 = play_game_recursive(player0, player1)
        if winner == 0:
            self.part_two_result = sum([val*(idx+1) for (idx, val) in enumerate(player0[::-1])])
        else:
            self.part_two_result = sum([val*(idx+1) for (idx, val) in enumerate(player1[::-1])])