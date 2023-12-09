from .base import Base


class Day9(Base):
    def __init__(self):
        self.day = 9

    def parse_input(self):
        data = super().get_input().split("\n")
        # data = super().get_test_input().split("\n")

        return [[int(n) for n in line.split()] for line in data]

    def part_1(self, data):
        def predict(line):
            diff = [line[i + 1] - line[i] for i in range(len(line) - 1)]

            if all(n == 0 for n in diff):
                return diff[-1] + line[-1]
            return predict(diff) + line[-1]

        return sum(predict(line) for line in data)

    def part_2(self, data):
        def predict(line):
            diff = [line[i + 1] - line[i] for i in range(len(line) - 1)]

            if all(n == 0 for n in diff):
                return line[0] - diff[0]
            return line[0] - predict(diff)

        return sum(predict(line) for line in data)
