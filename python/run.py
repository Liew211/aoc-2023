import sys
from setup import get_input
from solutions import (
    Base,
    Day1,
    Day2,
    Day3,
    Day4,
    Day5,
)


SOLUTIONS = [
    Base(),
    Day1(),
    Day2(),
    Day3(),
    Day4(),
    Day5(),
]


if __name__ == "__main__":
    SOLUTIONS[int(sys.argv[1])].run()
