from .base import Base


class Day1(Base):
    def __init__(self):
        self.day = 1

    def parse_input(self):
        return super().get_input().split("\n")

    def part_1(self, data):
        total = 0
        for line in data:
            stack = []
            for letter in line:
                if letter < "A":
                    stack.append(int(letter))
            total += stack[0] * 10 + stack[-1]

        return total

    def part_2(self, data):
        numbers = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        numbers.extend([str(i) for i in range(1, 10)])
        total = 0
        for line in data:
            left = [line.find(n) for n in numbers]
            right = [line.rfind(n) for n in numbers]
            l_index = 0
            l_val = len(line)

            for i, n in enumerate(left):
                # i is place in map
                # n is index of occurrence
                # need to find index of smallest value in list
                if n > -1 and n < l_val:
                    l_index, l_val = i, n
            r_index = 0
            r_val = -1
            for i, n in enumerate(right):
                if n > -1 and n > r_val:
                    r_index, r_val = i, n

            total += (l_index % 9 + 1) * 10 + (r_index % 9 + 1)

        return total
