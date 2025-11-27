from utils.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict

neighbors = [(-1,0), (1,0), (0, -1), (0,1)]

def next(grid, pos, old_pos):
    (yo, xo) = old_pos
    (y,x) = pos
    match grid[y][x]:
        case "|": 
            if yo == y-1: return (y+1, x)
            elif yo == y+1: return (y-1, x)
            else: return -1  
        case "-":
            if xo == x-1: return (y, x+1)
            elif xo == x+1: return (y, x-1)
            else: return -1 
        case "L": # east- north
            if yo == y-1: return (y, x+1)
            elif xo == x+1: return (y-1, x)
            else: return -1 
        case "J": # west- north
            if yo == y-1: return (y, x-1)
            elif xo == x-1: return (y-1, x)
            else: return -1 
        case "7": # west- south
            if xo == x-1: return (y+1, x)
            elif yo == y+1: return (y, x-1)
            else: return -1 
        case "F": # east - south
            if xo == x+1: return (y+1, x)
            elif yo == y+1: return (y, x+1)
            else: return -1 
        case ".": return -1
    return -1

def find_path(grid, start):
    for neighbor in neighbors:
        old_pos = start
        pos = (start[0]+neighbor[0], start[1]+neighbor[1])
        result = [old_pos, pos]
        while pos != start:
            tmp = next(grid, pos, old_pos)
            if tmp == -1: break
            old_pos = pos
            pos = tmp
            result.append(pos)
        if result[-1] == start: break
    return result


# advent of code 2023 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        grid = []
        for (y,line) in enumerate(self.data.splitlines()):
            tmp = []
            for (x,char) in enumerate(list(line)):
                tmp.append(char)
                if char == "S": start = (y,x)
            grid.append(tmp)
        self.parsed = (grid, start)

    def part_one(self):
        (grid, start) = self.parsed

        self.part_one_result = (len(find_path(grid, start)) - 1) // 2

    def part_two(self):
        (grid, start) = self.parsed
        path = find_path(grid, start)
        path = path[:-1]

        active_lists = {}
        for idx in range(0, len(grid)):
            tmp = [edge for edge in path if edge[0] == idx]
            if tmp != [] : active_lists[idx] = sorted(tmp, key=lambda x: x[1])
        
        cnt = 0
        for line in active_lists.keys():
            tmp = []
            for edge in active_lists[line]:
                if grid[edge[0]][edge[1]] == "-":
                     cnt += 1
                else: tmp.append(edge)

            active_list = tmp
            active_list.sort(key=lambda x: x[1])
            active_lists[line] = active_list

        result = 0
        for active_list in active_lists.values():

            for idx in range(0, len(active_list)-1, 2):
                if active_list[idx+1][1] != active_list[idx][1]:
                    result += active_list[idx+1][1] - active_list[idx][1] - 1
            
        self.part_two_result = result 