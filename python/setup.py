import requests
import toml
from pathlib import Path


for i in range(8, 26):
    with open(f"python/solutions/day_{i}.py", "w+") as f:
        f.write("""from .base import Base


class Day%d(Base):
    def __init__(self):
        self.day = %d

    def parse_input(self):
        data = super().get_input().split("\\n")
        # data = super().get_test_input().split("\\n")

        return data

    def part_1(self, data):
        total = 0

        return total

    def part_2(self, data):
        total = 0

        return total
""" % (i, i))
