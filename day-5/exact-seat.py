def load_input():
    return list(str(x.strip()) for x in open("input.txt"))


def solve(passes):
    seats = {}
    for p in passes:
        row = row_to_int(p[:7])
        col = col_to_int(p[7:])
        seats[(row * 8 + col)] = p
    seat_numbers = list(seats.keys())
    seat_numbers.sort()
    for x in range(len(seat_numbers)):
        if seat_numbers[x + 1] != seat_numbers[x] + 1:
            return seat_numbers[x] + 1


def int_to_id(seat):
    binary = bin(seat)[2:]
    print(binary)


def row_to_int(row_binary):
    total = 0
    for i in range(len(row_binary) - 1, -1, -1):
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
