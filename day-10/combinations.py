def load_input():
    return [0] + list(int(x.strip()) for x in open("input.txt"))


def count_connections(adapters, known_combinations):

    if len(adapters) == 1:  # Base case
        return 1

    for i, adapter in enumerate(adapters):
        if adapter in known_combinations:
            return known_combinations[adapter]
        else:
            viable = list(filter(lambda a: a <= adapters[i] + 3, adapters[i+1:i+4]))
            combinations = 0
            for n, next_adapter in enumerate(viable):
                if next_adapter in known_combinations:
                    combinations += known_combinations[next_adapter]
                else:
                    combinations += count_connections(adapters[i + n + 1:], known_combinations)
                    known_combinations[next_adapter] = combinations
            return combinations


adapter_data = load_input()
adapter_data.sort()
print(count_connections(adapter_data, {}))
