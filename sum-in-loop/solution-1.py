from time_benchmark import benchmark


def sum_in_loop(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum


@benchmark
def main():
    print(sum_in_loop(range(12345)))


if __name__ == '__main__':
    main()
