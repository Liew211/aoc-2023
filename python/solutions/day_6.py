import math

from .base import Base

from scipy.optimize import fsolve


class Day6(Base):
    def __init__(self):
        self.day = 6

    def parse_input(self):
        data = super().get_input().split("\n")
        # data = super().get_test_input().split("\n")

        return data

    def part_1(self, data):
        times = [int(n) for n in data[0].strip().split()[1:]]
        distances = [int(n) for n in data[1].strip().split()[1:]]
        margin = 1
        for i in range(len(times)):
            c = 0
            for j in range(times[i]):
                if (times[i] - j) * j > distances[i]:
                    c += 1
            margin *= c

        return margin

    def part_2(self, data):
        time = int("".join(data[0].strip().split()[1:]))
        distance = int("".join(data[1].strip().split()[1:]))
        
        f = lambda x: (time - x) * x - distance
        

        # print(f"{fsolve(f, [7700000, 38000000])}")
        sol = fsolve(f, [7700000, 38000000])
        
        
        return math.floor(sol[1]) - math.ceil(sol[0]) + 1
