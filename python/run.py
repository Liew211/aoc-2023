import argparse
from time import time
from solutions import *

SOLUTIONS = [
    Base(),
    Day1(),
    Day2(),
    Day3(),
    Day4(),
    Day5(),
    Day6(),
    Day7(),
    Day8(),
    Day9(),
    Day10(),
    Day11(),
    Day12(),
    Day13(),
    Day14(),
    Day15(),
    Day16(),
    Day17(),
    Day18(),
    Day19(),
    Day20(),
    Day21(),
    Day22(),
    Day23(),
    Day24(),
    Day25(),
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("day", type=int)
    parser.add_argument("-t", "--time", action="store_true")
    args = parser.parse_args()
    start = time()
    SOLUTIONS[args.day].run()
    if args.time:
        print(f"Ran in {(time() - start)*1000:.2f}ms")
