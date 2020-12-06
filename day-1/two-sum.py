def parse_input_to_set():
    return set(int(x) for x in open("sum-data.txt"))


def find_sum(entries, total):
    for n in entries:
        if total - n in entries:
            return n * (total - n)


data = parse_input_to_set()
print(find_sum(data, 2020))
