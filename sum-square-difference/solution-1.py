from time_benchmark import benchmark


def gen_square(max_num):
    for num in range(1, max_num):
        yield num ** 2


def get_squared_sum_and_sum_squared(upperlimit):
    squared_sum = sum(gen_square(upperlimit+1))
    sum_squared = sum(range(1, upperlimit+1)) ** 2
    return squared_sum, sum_squared


@benchmark
def main():
    squared_sum, sum_squared = get_squared_sum_and_sum_squared(100)
    print(f"difference between squared sum ({squared_sum}) and sum squared ({sum_squared}) is {sum_squared - squared_sum}")


if __name__ == '__main__':
    main()
