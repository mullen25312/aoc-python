from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
import copy
from itertools import product

from utils.tree import Tree


def build_path_tree(tree, used, caves, inv_caves, graph):
    for child in tree.children:

        tmp = copy.deepcopy(used)
        if not (child.upper() == child):
            tmp.add(child)

        if child != "end":
            for idx, reach in enumerate(graph[caves[child]]):
                if reach and (inv_caves[idx] not in tmp):
                    tree.children[child].add_child(inv_caves[idx])
            build_path_tree(tree.children[child], tmp, caves, inv_caves, graph)


def build_path_tree_two(tree, used, caves, inv_caves, graph):
    for child in tree.children:

        tmp = copy.deepcopy(used)
        if not (child.upper() == child):
            tmp[child] += 1

        if child != "end":
            for idx, reach in enumerate(graph[caves[child]]):
                if reach and ((tmp[inv_caves[idx]] == 0) or (tmp[inv_caves[idx]] == 1) and all(v <= 1 for v in iter(tmp.values()))):
                    tree.children[child].add_child(inv_caves[idx])
            build_path_tree_two(tree.children[child], tmp, caves, inv_caves, graph)


class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # parse input
        self.parsed = {"caves": {}, "inv_caves": {}, "graph": None}

        tmp = [line.split("-") for line in self.data.splitlines()]

        # parse caves
        idx = 0
        for conn in tmp:
            if conn[0] not in self.parsed["caves"].keys():
                self.parsed["caves"][conn[0]] = idx
                idx += 1
            if conn[1] not in self.parsed["caves"].keys():
                self.parsed["caves"][conn[1]] = idx
                idx += 1
        pass

        self.parsed["inv_caves"] = {y: x for x, y in self.parsed["caves"].items()}

        # construct graph as matrix to represent system of caves
        self.parsed["graph"] = np.zeros((len(self.parsed["caves"]), len(self.parsed["caves"])), dtype=bool)
        for conn in tmp:
            # symmetric matrix because all transitions are bidirectional
            self.parsed["graph"][self.parsed["caves"][conn[0]], self.parsed["caves"][conn[1]]] = True
            self.parsed["graph"][self.parsed["caves"][conn[1]], self.parsed["caves"][conn[0]]] = True

    def part_one(self):
        # build tree of possible paths
        # pathTree = {"start": Tree()}
        pathTree = Tree()
        pathTree.add_child("start")
        used = set(["start"])
        build_path_tree(pathTree, used, self.parsed["caves"], self.parsed["inv_caves"], self.parsed["graph"])
        self.part_one_result = pathTree.number_of_specific_leaves(specific="end")

    def part_two(self):
        pathTree = Tree()
        pathTree.add_child("start")
        used = dict(product(self.parsed["caves"], [0]))
        used["start"] = -2
        build_path_tree_two(pathTree, used, self.parsed["caves"], self.parsed["inv_caves"], self.parsed["graph"])
        self.part_two_result = pathTree.number_of_specific_leaves(specific="end")
