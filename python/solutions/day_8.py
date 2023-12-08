import numpy as np
from .base import Base


class Day8(Base):
    def __init__(self):
        self.day = 8

    def parse_input(self):
        data = super().get_input().split("\n\n")
        # data = super().get_test_input().split("\n\n")

        instruction = data[0]
        nodes = {
            line[0:3]: {"L": line[7:10], "R": line[12:15]}
            for line in data[1].split("\n")
        }
        return instruction, nodes

    def part_1(self, data):
        instruction, nodes = data

        count = 0
        curr = "AAA"
        while curr != "ZZZ":
            curr = nodes[curr][instruction[count % len(instruction)]]
            count += 1

        return count

    def part_2(self, data):
        instruction, nodes = data

        count = 0
        node = [n for n in nodes if n[2] == "A"]

        def get_count(node):
            count = 0
            curr = node
            while curr[2] != "Z":
                curr = nodes[curr][instruction[count % len(instruction)]]
                count += 1
            print(
                node,
                curr,
                count / len(instruction),
                nodes[curr][instruction[count % len(instruction)]],
            )
            return count

        counts = [get_count(c) for c in node]

        print([int(c / len(instruction)) for c in counts])

        return str(np.lcm.reduce(counts, dtype=np.longlong))
