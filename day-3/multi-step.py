def load_input():
    return list(str(x) for x in open("input.txt"))


def solve(data, h, v):
    count = 0
    position = 0
    for x in range(0, len(data), v):
        if data[x][position % 31] == '#':
            count += 1
        position += h
    return count


test_input = load_input()
print(solve(test_input, 1, 1) *
      solve(test_input, 3, 1) *
      solve(test_input, 5, 1) *
      solve(test_input, 7, 1) *
      solve(test_input, 1, 2))


