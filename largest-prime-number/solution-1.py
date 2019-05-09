from math import sqrt

from time_benchmark import benchmark


def gen_primes():
    p = 2
    while True:
        prime = True
        for i in range(2, int(sqrt(p) + 1)):
            if p % i == 0:
                prime = False
                break
        if prime:
            yield p
        p += 1


def find_largest_prime_factor(num: int) -> int:
    prime_gen = gen_primes()
    primes = set()
    prime = next(prime_gen)
    while True:
        if num % prime == 0:
            primes.add(prime)
            num /= prime
        else:
            prime = next(prime_gen)
        if prime > num:
            break
    return max(primes)


@benchmark
def main():
    prime = find_largest_prime_factor(600851475143)
    print(prime)


if __name__ == '__main__':
    main()
