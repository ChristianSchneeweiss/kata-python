from math import sqrt

from time_benchmark import benchmark


def is_prime(num):
    upper_limit = int(sqrt(num))
    for i in range(2, upper_limit + 1):
        if num % i == 0:
            return False
    return True


def gen_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


@benchmark
def main():
    sum = 0
    for prime in gen_prime():
        if prime > 2_000_000:
            break
        sum += prime
    print(f"sum of all primes up to 2 million is {sum}")


if __name__ == '__main__':
    main()
