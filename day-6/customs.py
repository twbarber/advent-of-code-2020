from functools import reduce


data = list(str(x.strip().replace('\n', '')) for x in open("input.txt").read().split("\n\n"))
print(reduce(lambda a, b: a + len(b), map(lambda d: set(d), data), 0))
