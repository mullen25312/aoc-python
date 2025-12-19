# advent of code website: https://adventofcode.com
# github: https://github.com/mullen25312/aoc-python

import os
import importlib
import itertools
import aocd

from timeit import default_timer as timer

# construct list of selected daily puzzles
dailyPuzzles = []
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y19"], range(1, 26))]) # year 2019
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y20"], range(1, 26))]) # year 2020
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y21"], range(1, 26))]) # year 2021
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y22"], range(1, 26))]) # year 2022
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y23"], range(1, 26))]) # year 2023
# dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y24"], range(1, 26))]) # year 2024
dailyPuzzles.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y25"], range(1, 9))]) # year 2025
dailyPuzzles.extend(["y25.d10", "y25.d11", "y25.d12"])
# dailyPuzzles.remove("y19.d07")
# dailyPuzzles = ["y23.d17"]


if __name__ == "__main__":

    durations_part_one = []; durations_part_two = []

    # run all selected daily puzzles
    for dailyPuzzle in dailyPuzzles:

        # import daily module
        try:
            importedModule = importlib.import_module(f"{dailyPuzzle}.dailyPuzzle")
        except ModuleNotFoundError:
            print(f"### {dailyPuzzle} ### : not implemented yet")
            continue

        # load demo data
        puzzle = importedModule.DailyPuzzle(os.path.join(dailyPuzzle.replace(".", "/"), "demo.txt"))

        # load or fetch input data
        if not os.path.exists(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt")):
            data = aocd.get_data(day=int(dailyPuzzle[5:7]), year=2000 + int(dailyPuzzle[1:3]))
            with open(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt"), "w") as file:
                file.write(data)
        puzzle = importedModule.DailyPuzzle(os.path.join(dailyPuzzle.replace(".", "/"), "input.txt"))


        # solve puzzle
        puzzle.parse()
        start = timer()
        puzzle.part_one()
        durations_part_one.append((timer() - start) * 1000)
        puzzle.part_two()
        durations_part_two.append((timer() - (start + durations_part_one[-1] / 1000)) * 1000)

        # print results
        print(f"### {dailyPuzzle} ### : {puzzle.part_one_result:15d} / {puzzle.part_two_result:15d}  in {durations_part_one[-1]:8.2f} / {durations_part_two[-1]:8.2f} ms")
    print(f"#### Total #### : {' '*37} {sum(durations_part_one):8.2f} / {sum(durations_part_two):8.2f} ms => {sum(durations_part_one) + sum(durations_part_two):8.2f} ms")