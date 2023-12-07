import re
from collections import defaultdict
from .base import Base


class Day3(Base):
    def __init__(self):
        self.day = 3

    def parse_input(self):
        return super().get_input().split("\n")

    def part_1(self, data):
        total = 0
        new_map = []
        for line in data:
            nums = [n for n in re.sub(r"[^0-9]", ".", line).split(".")]
            new_line = []
            for n in nums:
                if n:
                    new_line.append(n)
                    new_line.extend(["" for _ in range(len(n))])
                else:
                    new_line.append("")
            new_map.append(new_line)

        for i, line in enumerate(new_map):
            for j, point in enumerate(line):
                if point.isdigit() and self.check_symbol(data, i, j, len(point)):
                    total += int(point)

        return total

    def part_2(self, data):
        total = 0
        new_map = []
        for line in data:
            nums = [n for n in re.sub(r"[^0-9]", ".", line).split(".")]
            new_line = []
            for n in nums:
                if n:
                    new_line.append(n)
                    new_line.extend(["" for _ in range(len(n))])
                else:
                    new_line.append("")
            new_map.append(new_line)

        gear_map = defaultdict(list)
        for i, line in enumerate(new_map):
            for j, point in enumerate(line):
                if point.isdigit():
                    for k, v in self.find_symbols(data, i, j, point).items():
                        gear_map[k].extend(v)
        for g, v in gear_map.items():
            if len(v) == 2:
                total += v[0] * v[1]

        return total

    def check_symbol(self, data, i, j, length):
        for x in range(max(0, i - 1), min(len(data), i + 2)):
            for y in range(max(0, j - 1), min(len(data[0]), j + length + 1)):
                if re.match(r"[^0-9.]", data[x][y]):
                    return True
        return False

    def find_symbols(self, data, i, j, number):
        symbols = defaultdict(list)
        for x in range(max(0, i - 1), min(len(data), i + 2)):
            for y in range(max(0, j - 1), min(len(data[0]), j + len(number) + 1)):
                if re.match(r"[^0-9.]", data[x][y]):
                    symbols[f"{x},{y}"].append(int((number)))

        return symbols
