from utils.superDailyPuzzle import SuperDailyPuzzle
import math
from utils.intcode_computer import IntcodeComputer
from itertools import permutations

# advent of code 2019 day 7
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        lines = self.data.split(",")
        self.parsed = [int(line) for line in lines]

    def part_one(self):
        program = self.parsed.copy()

        # self.part_one_result = 0
        # return

        # initialize loop over all permutations of valid phase settings
        thruster_signals = []
        phase_setting_permutations = list(permutations(range(0, 5)))
        # phase_setting_permutations = [[0,1,2,3,4]]

        # loop over all permutations of valid phase settings
        for phase_settings in phase_setting_permutations:
            # initialize first amplifier (with input zero)
            amps = []
            amps.append(IntcodeComputer(program, [phase_settings[0], 0]))
            amps[0].run()

            # run all other amplifier (with input as output of the one before)
            for phase in phase_settings[1:]:
                amps.append(IntcodeComputer(program, [phase, amps[-1].outputs[0]]))
                amps[-1].run()

            # save thruster output for this permutation of valid phase settings
            thruster_signals.append(amps[-1].outputs[0])

        # return maximum thruster output
        self.part_one_result = max(thruster_signals)

    def part_two(self):
        program = self.parsed.copy()

        # self.part_two_result = 0
        # return

        # initialize loop over all permutations of valid phase settings
        thruster_signals = []
        phase_setting_permutations = list(permutations(range(5, 10)))

        ## loop over all permutations of valid phase settings
        for phase_settings in phase_setting_permutations:
            amps = []
            amps.append(IntcodeComputer(program, [phase_settings[0], 0]))
            amps[0].run()

            # first feed forward
            for phase in phase_settings[1:]:
                amps.append(IntcodeComputer(program, [phase, amps[-1].outputs[0]]))
                amps[-1].run()

            # run feddback until one of the amplifiers terminates
            while not any([amp.terminated() for amp in amps]):
                for idx, phase in enumerate(phase_settings):
                    amps[idx].inputs.append(amps[idx - 1].outputs[-1])
                    amps[idx].run()

            # save thruster output for this permutation of valid phase settings
            thruster_signals.append(amps[-1].outputs[-1])

        # return maximum thruster output
        self.part_two_result = max(thruster_signals)