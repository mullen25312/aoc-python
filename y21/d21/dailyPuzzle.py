from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
from functools import lru_cache
from itertools import product

quantum_die_triples = product((1, 2, 3), repeat=3)
quantum_die_cnt = [sum(triple) for triple in quantum_die_triples]
quantum_die_freq = {cnt: quantum_die_cnt.count(cnt) for cnt in quantum_die_cnt}


@lru_cache(maxsize=None)
def play_round(turn, player_scores, player_positions):

    if any(score >= 21 for score in player_scores):
        return np.array([1, 0]) if turn else np.array([0, 1])

    win = np.array([0, 0], dtype=np.int64)  # ensure that the number of universes fits !!!
    for throw, freq in quantum_die_freq.items():
        player_positions_new = ((player_positions[0] + throw * (turn == 0)) % 10, (player_positions[1] + throw * (turn == 1)) % 10)
        player_scores_new = (player_scores[0] + (player_positions_new[0] + 1) * (turn == 0), player_scores[1] + (player_positions_new[1] + 1) * (turn == 1))
        win += freq * play_round(1 - turn, player_scores_new, player_positions_new)
    return win


class deterministic_die:
    def __init__(self):
        self.state = -1

    def throw(self):
        self.state += 1
        return (self.state % 100) + 1


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = [int(line.split(":")[1]) - 1 for line in self.data.splitlines()]

    def part_one(self):
        player_scores = [0, 0]
        player_positions = self.parsed.copy()
        dice = deterministic_die()

        while True:
            player_positions[0] += sum([dice.throw(), dice.throw(), dice.throw()])
            player_scores[0] += (player_positions[0] % 10) + 1
            if player_scores[0] >= 1000:
                break

            player_positions[1] += sum([dice.throw(), dice.throw(), dice.throw()])
            player_scores[1] += (player_positions[1] % 10) + 1
            if player_scores[1] >= 1000:
                break

        self.part_one_result = min(player_scores) * (dice.state + 1)

    def part_two(self):
        self.part_two_result = max(play_round(0, (0, 0), tuple(self.parsed)))
