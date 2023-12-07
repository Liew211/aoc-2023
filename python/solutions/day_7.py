from functools import cmp_to_key
from .base import Base


class Day7(Base):
    def __init__(self):
        self.day = 7

    def parse_input(self):
        data = super().get_input().split("\n")
        # data = super().get_test_input().split("\n")

        return [line.split() for line in data]

    def part_1(self, data):
        data.sort(key=cmp_to_key(self.sorter))
        total = 0
        for i, player in enumerate(data):
            total += (len(data) - i) * int(player[1])

        return total

    def part_2(self, data):
        data.sort(key=cmp_to_key(self.sorter2))
        total = 0
        for i, player in enumerate(data):
            total += (len(data) - i) * int(player[1])

        return total

    def get_type(self, hand):
        cards = sorted([c for c in hand])
        if len(set(cards)) == 1:
            # 5 of a kind
            return 0
        if len(set(cards)) == 2:
            if (cards[0] == cards[1]) ^ (cards[3] == cards[4]):
                # 4 of a kind
                return 1
            # full house
            return 2
        if len(set(cards)) == 3:
            if any(cards.count(c) == 3 for c in cards):
                # 3 of a kind
                return 3
            # two pair
            return 4
        if len(set(cards)) == 4:
            # one pair
            return 5
        if len(set(cards)) == 5:
            # high card
            return 6

    def sorter(self, a, b):
        cards = {
            c: i
            for i, c in enumerate(
                ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
            )
        }
        if self.get_type(a[0]) != self.get_type(b[0]):
            return self.get_type(a[0]) - self.get_type(b[0])

        for i in range(5):
            if cards[a[0][i]] != cards[b[0][i]]:
                return cards[a[0][i]] - cards[b[0][i]]
        return 0

    def get_type2(self, hand):
        if hand == "JJJJJ":
            return 0
        temp = list(hand.replace("J", ""))
        hand = hand.replace("J", max(set(temp), key=temp.count))

        cards = sorted([c for c in hand])

        if len(set(cards)) == 1:
            # 5 of a kind
            return 0
        if len(set(cards)) == 2:
            if (cards[0] == cards[1]) ^ (cards[3] == cards[4]):
                # 4 of a kind
                return 1
            # full house
            return 2
        if len(set(cards)) == 3:
            if any(cards.count(c) == 3 for c in cards):
                # 3 of a kind
                return 3
            # two pair
            return 4
        if len(set(cards)) == 4:
            # one pair
            return 5
        if len(set(cards)) == 5:
            # high card
            return 6

    def sorter2(self, a, b):
        cards = {
            c: i
            for i, c in enumerate(
                ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
            )
        }
        if self.get_type2(a[0]) != self.get_type2(b[0]):
            return self.get_type2(a[0]) - self.get_type2(b[0])

        for i in range(5):
            if cards[a[0][i]] != cards[b[0][i]]:
                return cards[a[0][i]] - cards[b[0][i]]
        return 0
