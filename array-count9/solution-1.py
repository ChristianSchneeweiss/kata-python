from collections import Counter
from math import sqrt

from time_benchmark import benchmark


def array_count9(arr):
    return Counter(arr)[9]


@benchmark
def main():
    print(array_count9([1, 2, 9]))
    print(array_count9([1, 9, 9]))
    print(array_count9([1, 9, 9, 3, 9]))
    print(array_count9([1, 9, 9, 3, 9, 9, 9, 9, 9]))


if __name__ == '__main__':
    main()
