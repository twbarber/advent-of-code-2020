def load_input():
    return [int(x.strip()) for x in open("input.txt")]


def solve(adapters):
    adapters.sort()
    one_jolt_dif = 1
    three_jolt_diff = 1
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            one_jolt_dif += 1
        if adapters[i + 1] - adapters[i] == 3:
            three_jolt_diff += 1
    return one_jolt_dif * three_jolt_diff


adapter_data = load_input()
print(solve(adapter_data))