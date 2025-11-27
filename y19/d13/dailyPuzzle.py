from utils.superDailyPuzzle import SuperDailyPuzzle
import time
import sys
from utils.intcode_computer import IntcodeComputer

class Arcade:
    def __init__(self, programm):
        self.cpu = IntcodeComputer(programm)
        self.screen = {}
        self.score = 0

    def throw_in_quarters(self, number_of_quarters):
        self.cpu.program[0] = number_of_quarters

    def step(self):
        # run for x position
        self.cpu.run()
        x = self.cpu.outputs[-1]

        # run for y position
        self.cpu.run()
        y = self.cpu.outputs[-1]

        # run for tile id
        self.cpu.run()
        load = self.cpu.outputs[-1]

        if x == -1 and y == 0:
            self.score = load
        else:
            self.screen[(x, y)] = load

    def show_screen(self):
        # get maximum coordinates assuming robot stays in first quadrant
        xmax = max(self.screen.keys(), key=lambda item: item[0])[0]
        ymax = max(self.screen.keys(), key=lambda item: item[1])[1]

        # render output string
        output_str = [[*[" " for _ in range(xmax + 1)], "\n"] for _ in range(ymax + 1)]
        for pos in self.screen:
            if self.screen[pos] == 0:
                output_str[pos[1]][pos[0]] = " "
            elif self.screen[pos] == 1:
                output_str[pos[1]][pos[0]] = "\u2588"
            elif self.screen[pos] == 2:
                output_str[pos[1]][pos[0]] = "\u25a1"
            elif self.screen[pos] == 3:
                output_str[pos[1]][pos[0]] = "\u2585"
            elif self.screen[pos] == 4:
                output_str[pos[1]][pos[0]] = "\u25cf"

        output_str = [char for line in output_str for char in line]

        # return output string
        return "".join(output_str)

# advent of code 2019 day 13
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        # read input data
        lines = self.data.split(",")
        self.parsed = [int(line) for line in lines]

    def part_one(self):
        # start arcade
        arcade = Arcade(self.parsed.copy())

        # run arcade until terminated
        while not arcade.cpu.terminated():
            arcade.step()

        # return number of block tiles
        self.part_one_result = len([pos for pos, tile_id in arcade.screen.items() if tile_id == 2])

    def part_two(self):
        # start arcade
        arcade = Arcade(self.parsed.copy())
        arcade.throw_in_quarters(2)

        # initial drawing
        while len(arcade.screen) != 1035:
            arcade.step()

        # run game
        arcade.step()
        # print(arcade.show_screen())

        while not arcade.cpu.terminated():

            # bot modus
            tmp = [pos for pos, tile_id in arcade.screen.items() if tile_id == 4]
            b_pos = tmp[0]
            tmp = [pos for pos, tile_id in arcade.screen.items() if tile_id == 3]
            p_pos = tmp[0]

            if b_pos[0] < p_pos[0]:
                key = "a"
            elif b_pos[0] > p_pos[0]:
                key = "d"
            else:
                key = ""

            # manual modus
            # key = input("Joystick input: ")

            if key == "a":
                arcade.cpu.inputs.insert(0, -1)
                arcade.step()
                arcade.step()
                arcade.step()
                arcade.step()

            elif key == "d":
                arcade.cpu.inputs.insert(0, 1)
                arcade.step()
                arcade.step()
                arcade.step()
                arcade.step()

            else:
                arcade.cpu.inputs.insert(0, 0)
                arcade.step()
                arcade.step()

            # print(arcade.show_screen(), end="")
            # time.sleep(0.01)

        self.part_two_result = arcade.score