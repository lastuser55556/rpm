def linear(values, target):
    for comparisons, value in enumerate(values, 1):
        if value == target:
            return True, comparisons
    return False, len(values)


def binary(values, target):
    left, right = 0, len(values)
    probes = 0
    while left < right:
        middle = (left + right) // 2
        probes += 1
        if values[middle] == target:
            return True, probes
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return False, probes


if __name__ == "__main__":
    print("Размер | Линейный | Двоичный")
    for size in (10, 100, 1000, 10000):
        values = list(range(size))
        for key in (-1, 0, size // 2, size - 1, size):
            assert linear(values, key)[0] == binary(values, key)[0]
        assert not binary([], 0)[0]
        print(size, linear(values, size)[1], binary(values, size)[1], sep=" | ")
