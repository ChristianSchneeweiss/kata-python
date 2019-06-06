import numpy as np

from time_benchmark import benchmark


def digit_sum(num):
    digits = []
    while num > 0:
        num, digit = divmod(num, 10)
        digits.append(digit)
    return sum(digits)


@benchmark
def main():
    factorial = np.math.factorial(100)
    d_sum = digit_sum(factorial)
    print(d_sum)


if __name__ == '__main__':
    main()
