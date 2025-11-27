from utils.superDailyPuzzle import SuperDailyPuzzle

from ranges import Range, RangeSet

def mapping(value, ranges):
    for line in ranges:
        if value in range(line[1], line[2] + 1): 
            value = line[0] + (value-line[1])
            return value
    return value

def range_mapping(rngs, map_rngs): 
    for rng in rngs:  
        result = RangeSet()
        rng_tmp = RangeSet(Range(rng[0], rng[1], include_end=True))
        for map_rng in map_rngs:
            map_rng_tmp = Range(map_rng[1], map_rng[2], include_end=True)
            tmp = rng_tmp.intersection(map_rng_tmp)
            if not tmp.isempty():
                tmp2 = Range(tmp.ranges()[0].start + (map_rng[0]-map_rng[1]), tmp.ranges()[0].end + (map_rng[0]-map_rng[1]), include_end=True)
                result.add(tmp2)
                rng_tmp.difference_update(tmp2)
        result.add(rng_tmp)
    

# advent of code 2023 day 5
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)


    def parse(self):
        self.parsed = self.data.splitlines()

        self.seeds = [int(x.strip()) for x in (self.parsed[0].split(" "))[1:]]
        
        self.seed2soil = []
        self.soil2fertilizer = []
        self.fertilizer2water = []
        self.water2light = []
        self.light2temperature = []
        self.temperature2humidity = []
        self.humidity2location = []

        for idx in range(0, len(self.parsed)):
            if "seed-to-soil map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.seed2soil.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.seed2soil[-1][2] = self.seed2soil[-1][2] + self.seed2soil[-1][1] - 1
                    mapping += 1
                idx += mapping

            elif "soil-to-fertilizer map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.soil2fertilizer.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.soil2fertilizer[-1][2] = self.soil2fertilizer[-1][2] + self.soil2fertilizer[-1][1] -1
                    mapping += 1
                idx += mapping

            elif "fertilizer-to-water map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.fertilizer2water.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.fertilizer2water[-1][2] = self.fertilizer2water[-1][2] + self.fertilizer2water[-1][1]-1
                    mapping += 1
                idx += mapping+1

            elif "water-to-light map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.water2light.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.water2light[-1][2] = self.water2light[-1][2] + self.water2light[-1][1]-1
                    mapping += 1
                idx += mapping+1

            elif "light-to-temperature map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.light2temperature.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.light2temperature[-1][2] = self.light2temperature[-1][2] + self.light2temperature[-1][1]-1
                    mapping += 1
                idx += mapping+1

            elif "temperature-to-humidity map" in self.parsed[idx]:
                mapping = 1
                while self.parsed[idx+mapping] != '':
                    self.temperature2humidity.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.temperature2humidity[-1][2] = self.temperature2humidity[-1][2] + self.temperature2humidity[-1][1]-1
                    mapping += 1
                idx += mapping+1

            elif "humidity-to-location map" in self.parsed[idx]:
                mapping = 1
                while idx+mapping < len(self.parsed) and self.parsed[idx+mapping] != '':
                    self.humidity2location.append([int(x) for x in self.parsed[idx+mapping].split(" ")])
                    self.humidity2location[-1][2] = self.humidity2location[-1][2] + self.humidity2location[-1][1]-1
                    mapping += 1
                idx += mapping+1

    def part_one(self):
        results = []
        for seed in self.seeds:
            tmp = seed
            tmp = mapping(tmp, self.seed2soil)
            tmp = mapping(tmp, self.soil2fertilizer)
            tmp = mapping(tmp, self.fertilizer2water)
            tmp = mapping(tmp, self.water2light)
            tmp = mapping(tmp, self.light2temperature)
            tmp = mapping(tmp, self.temperature2humidity)
            tmp = mapping(tmp, self.humidity2location)
            results.append(tmp)
        self.part_one_result = min(results)

    def part_two(self):

        seeds = []
        for idx in range(0, len(self.seeds), 2):
            seeds.append((self.seeds[idx], self.seeds[idx] + self.seeds[idx+1]-1))

        # print(seeds)

        # rng1 = Range(0, 100, include_end=True)
        # rng2 = Range(50, 70, include_end=True)
        # print(rng1.intersection(rng2))

        # map_rngs_set = RangeSet(*[Range(map_rng[1], map_rng[2]) for map_rng in self.seed2soil])
        # print(map_rngs_set)

        # tmp = range_mapping([[50,98]], self.seed2soil) 
        # print(tmp)  

        self.part_two_result = 0
