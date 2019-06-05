from math import sqrt

from time_benchmark import benchmark


def sum_of_digits(num):
    digits = []
    while num > 0:
        digit = num % 10
        num = num // 10
        digits.append(digit)
    return sum(digits)


@benchmark
def main():
    num = 2 ** 1000
    print(f"Sum of digits of 2^1000 = {sum_of_digits(num)}")


if __name__ == '__main__':
    main()
