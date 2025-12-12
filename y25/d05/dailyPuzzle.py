from utils.superDailyPuzzle import SuperDailyPuzzle

import bisect

# advent of code 2025 day 5
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self):
        spans = []; ids = []
        sections = self.data.strip().split('\n\n')
        
        # first section contains spans
        for line in sections[0].splitlines():
            spans.append((int(line.split("-")[0]), int(line.split("-")[1])))
        
        # second section contains IDs
        for line in sections[1].splitlines():
            ids.append(int(line))

        self.parsed = (spans, ids)
    

    def part_one(self):
        spans, ids = self.parsed
        self.part_one_result = sum([1 for id in ids if any([start <= id <= end for start, end in spans])])

    def part_two(self): 
        spans, _ = self.parsed

        res_spans = []
        for start, end in spans:
            first_span = next((res_span for res_span in res_spans if res_span[0] <= start <= res_span[1]), None)
            second_span = next((res_span for res_span in res_spans if res_span[0] <= end <= res_span[1]), None)

            # NONE / NONE (might contain an exisiting span inside)
            if first_span is None and second_span is None:
                for span in res_spans:
                    if start <= span[0] and end >= span[1]:res_spans.remove(span)
                bisect.insort(res_spans, (start, end))

            # HIT / NONE
            if first_span and second_span is None:
                res_spans.remove(first_span)
                bisect.insort(res_spans, (min(first_span[0], start), max(first_span[1], end)))

            # NONE / HIT
            if first_span is None and second_span:
                res_spans.remove(second_span)
                bisect.insort(res_spans, (min(second_span[0], start), max(second_span[1], end)))

            # HIT / HIT (only relevant if they are different)
            if first_span and second_span and first_span != second_span:
                first_span_index = res_spans.index(first_span)
                second_span_index = res_spans.index(second_span)
                del res_spans[first_span_index:second_span_index+1]
                bisect.insort(res_spans, (min(first_span[0], start), max(second_span[1], end)))

        self.part_two_result = sum([span[1] - span[0] + 1 for span in res_spans])