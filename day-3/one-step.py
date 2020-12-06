def load_input():
    return list(str(x) for x in open("input.txt"))


def solve(data):
    count = 0
    position = 0
    for x in data:
        if x[position % 31] == '#':
            count += 1
        position += 3
    return count


test_input = load_input()
print(solve(test_input))


