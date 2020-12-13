from itertools import combinations


def load_input():
    return [int(x.strip()) for x in open("input.txt")]


def solve(data):
    for i in range(25, len(data)):
        combos = list(combinations(data[i-25:i], 2))
        sums = list(map(lambda x: sum(x), list(combos)))
        if data[i] not in sums:
            return data[i]


cypher_input = load_input()
print(solve(cypher_input))
