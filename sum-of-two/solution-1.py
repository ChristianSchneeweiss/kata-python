from time_benchmark import benchmark


def sum_of_two(*args):
    return sum(args)


@benchmark
def main():
    print(sum_of_two(1, 4))
    print(sum_of_two(123, 41))
    print(sum_of_two(134, 4211))
    print(sum_of_two(167, 8456))


if __name__ == '__main__':
    main()
