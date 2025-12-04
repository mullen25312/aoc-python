import pytest
import yaml
import importlib
import os
import aocd

import itertools

# tests to run
days_to_be_tested = []
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y19"], range(1, 26))]) # year 2019
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y20"], range(1, 26))]) # year 2020
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y21"], range(1, 26))]) # year 2021
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y22"], range(1, 26))]) # year 2022
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y23"], range(1, 26))]) # year 2023
# days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y24"], range(1, 26))]) # year 2024
days_to_be_tested.extend([f"{year}.d{day:02d}" for year, day in itertools.product(["y25"], range(1, 5))]) # year 2025
# days_to_be_tested.remove("y24.d09")
# days_to_be_tested = ["y24.d01"]

# scenarios = ["demo", "input"]
scenarios = ["input"]

ids = tuple(f"{id[1]} -> {id[0]}" for id in itertools.product(days_to_be_tested, scenarios))


class TestConfig:
    __test__ = False

    def __init__(self, puzzle):
        self.aocd = aocd.models.Puzzle(year=2000 + int(puzzle[1:3]), day=int(puzzle[5:7]))

@pytest.fixture(scope="class", params=itertools.product(days_to_be_tested, scenarios), ids=ids)
def prepare_test(request):
    try:
        importedModule = importlib.import_module(f"{request.param[0]}.dailyPuzzle")
    except ModuleNotFoundError:
        pytest.skip(f"### {request.param[0]} ### : not implemented yet")

    if not os.path.exists(os.path.join(request.param[0].replace(".", "/"), f"{request.param[1]}.txt")):
        data = aocd.get_data(day=int(request.param[0][5:7]), year=2000 + int(request.param[0][1:3]))
        with open(os.path.join(request.param[0].replace(".", "/"), f"{request.param[1]}.txt"), "w") as file:
            file.write(data)
        
    request.cls.puzzle = importedModule.DailyPuzzle(os.path.join(request.param[0].replace(".", "/"), f"{request.param[1]}.txt"))
    request.cls.test_config = TestConfig(request.param[0])

@pytest.mark.usefixtures("prepare_test")
class Tests_dxx:

    def test_part_one(self):
        try:
            self.test_config.aocd.answer_a
        except AttributeError:
            pytest.skip("not solved yet")

        self.puzzle.parse()
        self.puzzle.part_one()
        assert  self.test_config.aocd.answer_a in (str(self.puzzle.part_one_result),  '')

    def test_part_two(self):
        try:
            self.test_config.aocd.answer_b
        except AttributeError:
            pytest.skip("not solved yet")

        self.puzzle.parse()
        self.puzzle.part_one() # in case results from part one are needed for part two
        self.puzzle.part_two()
        assert self.test_config.aocd.answer_b in (str(self.puzzle.part_two_result),  '') 
