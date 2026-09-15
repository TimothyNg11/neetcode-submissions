from collections import Counter, defaultdict

class CountSquares:
    def __init__(self):
        self.cnt = Counter()          # (x, y) -> multiplicity
        self.cols = defaultdict(set)  # x -> set of y values

    def add(self, point):
        x, y = point
        self.cnt[(x, y)] += 1
        self.cols[x].add(y)

    def count(self, point):
        x, y = point
        total = 0
        for b in self.cols[x]:
            d = b - y
            if d == 0:
                continue
            for nx in (x + d, x - d):
                total += (self.cnt[(x, b)]
                          * self.cnt[(nx, y)]
                          * self.cnt[(nx, b)])
        return total