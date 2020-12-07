from functools import reduce


data = list(str(x.strip().replace('\n', ',')).split(',') for x in open("input.txt").read().split("\n\n"))
print(reduce(lambda a, b: a + len(b), map(lambda d: reduce(lambda a, b: set(a) & set(b), d), data), 0))
