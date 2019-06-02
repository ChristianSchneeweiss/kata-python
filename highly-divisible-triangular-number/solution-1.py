from math import sqrt, ceil

from time_benchmark import benchmark


def gen_triangle_number():
    i = 2
    triangle_number = 1
    while True:
        yield triangle_number
        triangle_number += i
        i += 1


def get_divisors(num):
    highest = ceil(num / 2)
    divs = [i for i in range(1, highest + 1) if num % i == 0]
    divs.append(num)
    return divs


@benchmark
def main():
    for num in gen_triangle_number():
        divisors = get_divisors(num)
        if len(divisors) > 500:
            print(num, divisors, len(divisors))


if __name__ == '__main__':
    main()
