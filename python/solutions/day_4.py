from .base import Base


class Day4(Base):
    def __init__(self):
        self.day = 4

    def parse_input(self):
        return super().get_input().split("\n")

    def part_1(self, data):
        total = 0
        for line in data:
            _, d = line.split(":")
            winning, you = d.strip().split("|")
            
            winning_nums = set(int(n) for n in winning.split())
            your_nums = set(int(n) for n in you.split())
            total += int(2**(len([n for n in your_nums if n in winning_nums])-1))

        return total

    def part_2(self, data):
        num_cards = [1 for n in range(len(data))]
        for i, line in enumerate(data):
            _, d = line.split(":")
            winning, you = d.strip().split("|")
            
            winning_nums = set(int(n) for n in winning.split())
            your_nums = set(int(n) for n in you.split())

            for j in range(i+1, i + 1 + len([n for n in your_nums if n in winning_nums])):
                num_cards[j] += num_cards[i]

        return sum(num_cards)

