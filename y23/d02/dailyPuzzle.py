from utils.superDailyPuzzle import SuperDailyPuzzle

import numpy as np
       
# advent of code 2023 day 2
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):

        ## games
        games = []
        for line in self.data.splitlines():
            tmp = (line.split(":")[1]).split(";")
            ## reaches
            reaches = []
            for reach in tmp:
                tmp2 = reach.split(",")
                tmp3 = [entry.strip() for entry in tmp2]
                ## colors
                colors = {"blue":0, "green":0, "red":0}
                for entry in tmp3:
                    tmp4 = entry.split(" ")
                    colors[tmp4[1]] = int(tmp4[0])
                reaches.append(colors)
            games.append(reaches)

        # print(games)
        self.parsed = games

    def part_one(self):
                     
        max_colors = {"blue":14, "green":13, "red":12}
        sum = 0; id = 0

        for game in self.parsed:
            id += 1; possible = True
            for reach in game:
                if not((reach["blue"] <= max_colors["blue"]) and (reach["green"] <= max_colors["green"]) and (reach["red"] <= max_colors["red"])):
                    possible = False

            if possible == True: sum += id

        self.part_one_result = sum

    def part_two(self):

        sum = 0
        for game in self.parsed:
            min_colors = {"blue":0, "green":0, "red":0}
            for reach in game:
                if reach["blue"] > min_colors["blue"]: min_colors["blue"] = reach["blue"]
                if reach["green"] > min_colors["green"]: min_colors["green"] = reach["green"]
                if reach["red"] > min_colors["red"]: min_colors["red"] = reach["red"]
            sum += min_colors["blue"] * min_colors["green"] * min_colors["red"]
            
        self.part_two_result = sum
