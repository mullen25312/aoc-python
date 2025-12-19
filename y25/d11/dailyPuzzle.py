from platform import node
from utils.superDailyPuzzle import SuperDailyPuzzle

from utils.dijkstra import AbstractDijkstraSPF
from collections import defaultdict

from functools import lru_cache
from frozendict import frozendict


class DijkstraSPF(AbstractDijkstraSPF):
    @staticmethod
    def get_adjacent_nodes(G, u):
        return G[u]

    @staticmethod
    def get_edge_weight(G, u, v):
        return 1
        
@lru_cache(maxsize=None)
def dfs(paths, start, end, to_be_visited, visited):
    if start == end  and all(visited):
        return 1
    else:
        total = 0
        for adj in paths[start]:
            visited_new = tuple(visited[idx] or (adj == to_visit) for idx, to_visit in enumerate(to_be_visited))
            total += dfs(paths, adj, end, to_be_visited, visited_new)
        return total

# advent of code 2025 day 11
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        paths = defaultdict(tuple)
        for line in self.data.splitlines():
            tmp = line.split(" ")
            paths[tmp[0][:-1]] = tuple(tmp[1:])

        paths["out"] = ()
        self.parsed = paths
    
    def part_one(self):
        paths = self.parsed
        self.part_one_result = DijkstraSPF(paths, "you").get_number_of_paths("out")

    def part_two(self):
        paths = self.parsed
        self.part_two_result = dfs(frozendict(paths), "svr", "out", ("fft", "dac"), (False, False))
        


        
