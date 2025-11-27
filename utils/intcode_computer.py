from collections import defaultdict

# parameter modes: postion, immediate and relative
p_mode = {"pos": 0, "imm": 1, "rel": 2}


class IntcodeComputer:
    def __init__(self, program, inputs=[]):
        self.opcodes = {
            # addition
            1: (self.addition, (p_mode["pos"], p_mode["pos"], p_mode["pos"])),
            1001: (self.addition, (p_mode["pos"], p_mode["imm"], p_mode["pos"])),
            2001: (self.addition, (p_mode["pos"], p_mode["rel"], p_mode["pos"])),
            101: (self.addition, (p_mode["imm"], p_mode["pos"], p_mode["pos"])),
            1101: (self.addition, (p_mode["imm"], p_mode["imm"], p_mode["pos"])),
            2101: (self.addition, (p_mode["imm"], p_mode["rel"], p_mode["pos"])),
            201: (self.addition, (p_mode["rel"], p_mode["pos"], p_mode["pos"])),
            1201: (self.addition, (p_mode["rel"], p_mode["imm"], p_mode["pos"])),
            2201: (self.addition, (p_mode["rel"], p_mode["rel"], p_mode["pos"])),
            20001: (self.addition, (p_mode["pos"], p_mode["pos"], p_mode["rel"])),
            21001: (self.addition, (p_mode["pos"], p_mode["imm"], p_mode["rel"])),
            22001: (self.addition, (p_mode["pos"], p_mode["rel"], p_mode["rel"])),
            20101: (self.addition, (p_mode["imm"], p_mode["pos"], p_mode["rel"])),
            21101: (self.addition, (p_mode["imm"], p_mode["imm"], p_mode["rel"])),
            22101: (self.addition, (p_mode["imm"], p_mode["rel"], p_mode["rel"])),
            20201: (self.addition, (p_mode["rel"], p_mode["pos"], p_mode["rel"])),
            21201: (self.addition, (p_mode["rel"], p_mode["imm"], p_mode["rel"])),
            22201: (self.addition, (p_mode["rel"], p_mode["rel"], p_mode["rel"])),
            # muliplication
            2: (self.mulitplication, (p_mode["pos"], p_mode["pos"], p_mode["pos"])),
            1002: (self.mulitplication, (p_mode["pos"], p_mode["imm"], p_mode["pos"])),
            2002: (self.mulitplication, (p_mode["pos"], p_mode["rel"], p_mode["pos"])),
            102: (self.mulitplication, (p_mode["imm"], p_mode["pos"], p_mode["pos"])),
            1102: (self.mulitplication, (p_mode["imm"], p_mode["imm"], p_mode["pos"])),
            2102: (self.mulitplication, (p_mode["imm"], p_mode["rel"], p_mode["pos"])),
            202: (self.mulitplication, (p_mode["rel"], p_mode["pos"], p_mode["pos"])),
            1202: (self.mulitplication, (p_mode["rel"], p_mode["imm"], p_mode["pos"])),
            2202: (self.mulitplication, (p_mode["rel"], p_mode["rel"], p_mode["pos"])),
            20002: (self.mulitplication, (p_mode["pos"], p_mode["pos"], p_mode["rel"])),
            21002: (self.mulitplication, (p_mode["pos"], p_mode["imm"], p_mode["rel"])),
            22002: (self.mulitplication, (p_mode["pos"], p_mode["rel"], p_mode["rel"])),
            20102: (self.mulitplication, (p_mode["imm"], p_mode["pos"], p_mode["rel"])),
            21102: (self.mulitplication, (p_mode["imm"], p_mode["imm"], p_mode["rel"])),
            22102: (self.mulitplication, (p_mode["imm"], p_mode["rel"], p_mode["rel"])),
            20202: (self.mulitplication, (p_mode["rel"], p_mode["pos"], p_mode["rel"])),
            21202: (self.mulitplication, (p_mode["rel"], p_mode["imm"], p_mode["rel"])),
            22202: (self.mulitplication, (p_mode["rel"], p_mode["rel"], p_mode["rel"])),
            # input
            3: (self.input, (p_mode["pos"],)),
            103: (self.input, (p_mode["imm"],)),
            203: (self.input, (p_mode["rel"],)),
            # output
            4: (self.output, (p_mode["pos"],)),
            104: (self.output, (p_mode["imm"],)),
            204: (self.output, (p_mode["rel"],)),
            # jump if true
            5: (self.jump_if_true, (p_mode["pos"], p_mode["pos"])),
            1005: (self.jump_if_true, (p_mode["pos"], p_mode["imm"])),
            2005: (self.jump_if_true, (p_mode["pos"], p_mode["rel"])),
            105: (self.jump_if_true, (p_mode["imm"], p_mode["pos"])),
            1105: (self.jump_if_true, (p_mode["imm"], p_mode["imm"])),
            2105: (self.jump_if_true, (p_mode["imm"], p_mode["rel"])),
            205: (self.jump_if_true, (p_mode["rel"], p_mode["pos"])),
            1205: (self.jump_if_true, (p_mode["rel"], p_mode["imm"])),
            2205: (self.jump_if_true, (p_mode["rel"], p_mode["rel"])),
            # jump if false
            6: (self.jump_if_false, (p_mode["pos"], p_mode["pos"])),
            1006: (self.jump_if_false, (p_mode["pos"], p_mode["imm"])),
            2006: (self.jump_if_false, (p_mode["pos"], p_mode["rel"])),
            106: (self.jump_if_false, (p_mode["imm"], p_mode["pos"])),
            1106: (self.jump_if_false, (p_mode["imm"], p_mode["imm"])),
            2106: (self.jump_if_false, (p_mode["imm"], p_mode["rel"])),
            206: (self.jump_if_false, (p_mode["rel"], p_mode["pos"])),
            1206: (self.jump_if_false, (p_mode["rel"], p_mode["imm"])),
            2206: (self.jump_if_false, (p_mode["rel"], p_mode["rel"])),
            # less than
            7: (self.less_than, (p_mode["pos"], p_mode["pos"], p_mode["pos"])),
            1007: (self.less_than, (p_mode["pos"], p_mode["imm"], p_mode["pos"])),
            2007: (self.less_than, (p_mode["pos"], p_mode["rel"], p_mode["pos"])),
            107: (self.less_than, (p_mode["imm"], p_mode["pos"], p_mode["pos"])),
            1107: (self.less_than, (p_mode["imm"], p_mode["imm"], p_mode["pos"])),
            2107: (self.less_than, (p_mode["imm"], p_mode["rel"], p_mode["pos"])),
            207: (self.less_than, (p_mode["rel"], p_mode["pos"], p_mode["pos"])),
            1207: (self.less_than, (p_mode["rel"], p_mode["imm"], p_mode["pos"])),
            2207: (self.less_than, (p_mode["rel"], p_mode["rel"], p_mode["pos"])),
            20007: (self.less_than, (p_mode["pos"], p_mode["pos"], p_mode["rel"])),
            21007: (self.less_than, (p_mode["pos"], p_mode["imm"], p_mode["rel"])),
            22007: (self.less_than, (p_mode["pos"], p_mode["rel"], p_mode["rel"])),
            20107: (self.less_than, (p_mode["imm"], p_mode["pos"], p_mode["rel"])),
            21107: (self.less_than, (p_mode["imm"], p_mode["imm"], p_mode["rel"])),
            22107: (self.less_than, (p_mode["imm"], p_mode["rel"], p_mode["rel"])),
            20207: (self.less_than, (p_mode["rel"], p_mode["pos"], p_mode["rel"])),
            21207: (self.less_than, (p_mode["rel"], p_mode["imm"], p_mode["rel"])),
            22207: (self.less_than, (p_mode["rel"], p_mode["rel"], p_mode["rel"])),
            # equals
            8: (self.equals, (p_mode["pos"], p_mode["pos"], p_mode["pos"])),
            1008: (self.equals, (p_mode["pos"], p_mode["imm"], p_mode["pos"])),
            2008: (self.equals, (p_mode["pos"], p_mode["rel"], p_mode["pos"])),
            108: (self.equals, (p_mode["imm"], p_mode["pos"], p_mode["pos"])),
            1108: (self.equals, (p_mode["imm"], p_mode["imm"], p_mode["pos"])),
            2108: (self.equals, (p_mode["imm"], p_mode["rel"], p_mode["pos"])),
            208: (self.equals, (p_mode["rel"], p_mode["pos"], p_mode["pos"])),
            1208: (self.equals, (p_mode["rel"], p_mode["imm"], p_mode["pos"])),
            2208: (self.equals, (p_mode["rel"], p_mode["rel"], p_mode["pos"])),
            20008: (self.equals, (p_mode["pos"], p_mode["pos"], p_mode["rel"])),
            21008: (self.equals, (p_mode["pos"], p_mode["imm"], p_mode["rel"])),
            22008: (self.equals, (p_mode["pos"], p_mode["rel"], p_mode["rel"])),
            20108: (self.equals, (p_mode["imm"], p_mode["pos"], p_mode["rel"])),
            21108: (self.equals, (p_mode["imm"], p_mode["imm"], p_mode["rel"])),
            22108: (self.equals, (p_mode["imm"], p_mode["rel"], p_mode["rel"])),
            20208: (self.equals, (p_mode["rel"], p_mode["pos"], p_mode["rel"])),
            21208: (self.equals, (p_mode["rel"], p_mode["imm"], p_mode["rel"])),
            22208: (self.equals, (p_mode["rel"], p_mode["rel"], p_mode["rel"])),
            # relative base
            9: (self.adjust_relative_base, (p_mode["pos"],)),
            109: (self.adjust_relative_base, (p_mode["imm"],)),
            209: (self.adjust_relative_base, (p_mode["rel"],)),
            # termination
            99: (self.terminate, None),
        }
        self.ptr = 0
        self.program = defaultdict(int, {i: program[i] for i in range(0, len(program))})
        self.inputs = inputs
        self.outputs = []
        self.relative_base = 0

    def parse_parameter(self, parameter_modes):
        params = list(parameter_modes)
        for idx, param_mode in enumerate(parameter_modes):
            if param_mode == p_mode["pos"]:
                params[idx] = self.program[self.ptr + idx + 1]
            elif param_mode == p_mode["imm"]:
                params[idx] = self.ptr + idx + 1
            elif param_mode == p_mode["rel"]:
                params[idx] = self.relative_base + self.program[self.ptr + idx + 1]
        return params

    def addition(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)
        self.program[params[2]] = self.program[params[0]] + self.program[params[1]]

        self.ptr += 4
        return True

    def mulitplication(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)
        self.program[params[2]] = self.program[params[0]] * self.program[params[1]]

        self.ptr += 4
        return True

    def input(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)
        self.program[params[0]] = self.inputs.pop(0)

        self.ptr += 2
        return True

    def output(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)
        self.outputs.append(self.program[params[0]])

        self.ptr += 2
        return False

    def jump_if_true(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)

        if self.program[params[0]] != 0:
            self.ptr = self.program[params[1]]
        else:
            self.ptr += 3
        return True

    def jump_if_false(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)

        if self.program[params[0]] == 0:
            self.ptr = self.program[params[1]]
        else:
            self.ptr += 3
        return True

    def less_than(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)

        if self.program[params[0]] < self.program[params[1]]:
            self.program[params[2]] = 1
        else:
            self.program[params[2]] = 0

        self.ptr += 4
        return True

    def equals(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)

        if self.program[params[0]] == self.program[params[1]]:
            self.program[params[2]] = 1
        else:
            self.program[params[2]] = 0

        self.ptr += 4
        return True

    def adjust_relative_base(self, parameter_modes):
        params = self.parse_parameter(parameter_modes)
        self.relative_base = self.relative_base + self.program[params[0]]

        self.ptr += 2
        return True

    def terminate(self, not_used):
        return False

    def run(self):
        while True:
            handle, params = self.opcodes[self.program[self.ptr]]
            if handle(params) == False:
                break

    def run_until_termination(self):
        while True:
            handle, params = self.opcodes[self.program[self.ptr]]
            if handle(params) == False and handle == self.terminate:
                break

    def terminated(self):
        return self.program[self.ptr] == 99
