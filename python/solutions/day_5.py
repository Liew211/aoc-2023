from .base import Base


class Day5(Base):
    def __init__(self):
        self.day = 5

    def parse_input(self):
        data = super().get_input().split("\n\n")
        # data = super().get_test_input().split("\n\n")

        seeds = [int(n) for n in data[0].strip().split()[1:]]

        map_texts = [
            d.strip().split("\n")[1:] for d in data[1:]
        ]
        maps = [
            [[int(n) for n in line.split()] for line in m] for m in map_texts
        ]

        return seeds, maps

    def part_1(self, data):
        seeds, maps = data

        def get_location(seed):
            current_val = seed
            
            for map in maps:
                for line in map:
                    if current_val >= line[1] and current_val - line[1] < line[2]:
                        current_val += line[0] - line[1]
                        break

            return current_val

        locations = [get_location(s) for s in seeds]

        return min(locations)

    def part_2(self, data):
        seeds, maps = data

        def get_location(ranges):
            current_vals = ranges
            
            for map in maps:
                stack = current_vals
                current_vals = []
                while len(stack) > 0:
                    r = stack.pop()
                    
                    l = len(current_vals)
                    for line in map:
                        # range >= bottom of map
                        if r[0] >= line[1]:
                            # range ends before top of map
                            if r[1] - line[1] <= line[2]:
                                current_vals.append([r[0] + line[0] - line[1], r[1] + line[0] - line[1]])
                                break
                            # range ends after top of map but still has overlap
                            elif r[0] - line[1] < line[2]:
                                current_vals.append([r[0] + line[0] - line[1], line[0] + line[2]])
                                stack.append([line[1] + line[2], r[1]])
                                break

                        # range starts before bottom of map and ends after top of map
                        elif r[1] - line[1] > line[2]:
                            current_vals.append([line[0], line[0] + line[2]])
                            stack.append([line[1] + line[2], r[1]])
                            stack.append([r[0], line[1]])
                            break
                            
                        elif r[1] > line[1]:
                            current_vals.append([line[0], r[1] + line[0] - line[1]])
                            stack.append([r[0], line[1]])
                            break
                    if len(current_vals) == l:
                        current_vals.append(r)
            return min([r[0] for r in current_vals])

        min_location = 910845529
        for i in range(0, len(seeds), 2):
            ranges = [[seeds[i], seeds[i] + seeds[i + 1]]]
            range_min = get_location(ranges)
            min_location = min(min_location, range_min)

        
        return min_location
