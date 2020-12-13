from itertools import combinations


def load_input():
    return [int(x.strip()) for x in open("input.txt")]


def solve(data):
    for i in range(25, len(data)):
        combos = list(combinations(data[i-25:i], 2))
        sums = list(map(lambda x: sum(x), list(combos)))
        if data[i] not in sums:
            number = data[i]
            data.remove(data[i])
            return find_consecutive_sum(number, data[:i])


def find_consecutive_sum(num, data):
    i = 0
    start = i
    rolling_sum = 0
    while i < len(data):
        rolling_sum += data[i]
        if rolling_sum < num:
            i += 1
        if rolling_sum > num:
            i = start + 1
            start += 1
            rolling_sum = 0
        elif rolling_sum == num:
            return min(data[start:i + 1]) + max(data[start:i + 1])


cypher_input = load_input()
print(solve(cypher_input))
