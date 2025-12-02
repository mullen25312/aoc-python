# advent of code website: https://adventofcode.com
# github: https://github.com/mullen25312/aoc-python

import os
import importlib
import itertools
import aocd

# construct list of selected daily puzzles
dailyPuzzles = []
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y19"], range(1, 26))]) # year 2019
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y20"], range(1, 26))]) # year 2020
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y21"], range(1, 26))]) # year 2021
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y22"], range(1, 26))]) # year 2022
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y23"], range(1, 26))]) # year 2023
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y24"], range(1, 26))]) # year 2024
dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y25"], range(1, 26))]) # year 2025
# dailyPuzzles.remove("y19.d07")
# dailyPuzzles = ["y23.d17"]


if __name__ == "__main__":

    # run all selected daily puzzles
    for dailyPuzzle in dailyPuzzles:

        # import daily module
        try:
            importedModule = importlib.import_module(f"{dailyPuzzle}.dailyPuzzle")
        except ModuleNotFoundError:
            print(f"### {dailyPuzzle} ### : not implemented yet")
            continue

        # load demo data
        # puzzle = importedModule.DailyPuzzle(os.path.join(dailyPuzzle.replace(".", "/"), "demo.txt"))

        # load or fetch input data
        if not os.path.exists(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt")):
            data = aocd.get_data(day=int(dailyPuzzle[5:7]), year=2000 + int(dailyPuzzle[1:3]))
            with open(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt"), "w") as file:
                file.write(data)
        puzzle = importedModule.DailyPuzzle(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt"))

        # solve puzzle
        puzzle.parse()
        puzzle.part_one()
        puzzle.part_two()

        # print results
        print(f"### {dailyPuzzle} ### : " + str(puzzle.part_one_result) + " / " + str(puzzle.part_two_result))