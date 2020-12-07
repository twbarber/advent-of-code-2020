def load_input():
    return list(str(x.strip()) for x in open("input.txt"))


def solve(passes):
    highest = 0
    for p in passes:
        row_binary = p[:7]
        row = row_to_int(row_binary)
        col_binary = p[7:]
        col = col_to_int(col_binary)
        seat = row * 8 + col
        if seat > highest:
            highest = seat
    return highest


def row_to_int(row_binary):
    total = 0
    for i in range(len(row_binary)-1, -1, -1):
        if row_binary[i] == 'B':
            total += 2**(len(row_binary) - 1 - i)
    return total


def col_to_int(col_binary):
    total = 0
    for i in range(len(col_binary) - 1, -1, -1):
        if col_binary[i] == 'R':
            total += 2 ** (len(col_binary) - 1 - i)
    return total


boarding_passes = load_input()
print(solve(boarding_passes))
