from .base import Base


class Day3(Base):
    def __init__(self):
        self.day = 3

    def parse_input(self):
        return super().get_input().split("\n")

    def part_1(self, data):
        total = 0
        for i, line in enumerate(data):
            possible = True
            _, records = line.split(":")
            for r in records.strip().split(";"):
                for s in r.split(","):
                    num, color = s.strip().split()
                    if color == "red":
                        if int(num) > 12:
                            possible = False
                    if color == "green":
                        if int(num) > 13:
                            possible = False
                    if color == "blue":
                        if int(num) > 14:
                            possible = False
            if possible:
                total += i + 1

        return total

    def part_2(self, data):
        total = 0
        for i, line in enumerate(data):
            red = 0
            blue = 0
            green = 0
            _, records = line.split(":")
            for r in records.strip().split(";"):
                for s in r.split(","):
                    num, color = s.strip().split()
                    if color == "red":
                        if int(num) > red:
                            red = int(num)
                    if color == "green":
                        if int(num) > green:
                            green = int(num)
                    if color == "blue":
                        if int(num) > blue:
                            blue = int(num)
            total += red * blue * green

        return total
