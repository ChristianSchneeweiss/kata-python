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
    index = 1
    while True:
        if is_prime(num):
            yield num, index
            index += 1
        num += 1


@benchmark
def main():
    for prime, index in gen_prime():
        if index == 10001:
            print(f"{prime} is the {index} prime")
            break


if __name__ == '__main__':
    main()
