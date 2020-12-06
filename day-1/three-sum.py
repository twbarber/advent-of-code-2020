def parse_input_to_set():
    return set(int(x) for x in open("sum-data.txt"))


def find_sum(operands, entries, total):
    for n in entries:
        if total - n in entries and operands == 2:
            return n * (total - n)
        elif len(entries) > 2:
            attempt = find_sum(operands - 1, entries.copy().remove(n), total - n)
            if attempt is not None:
                return n * attempt
            else:
                continue


data = parse_input_to_set()
print(find_sum(3, data, 2020))
