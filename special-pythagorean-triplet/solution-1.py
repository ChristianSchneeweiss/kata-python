from math import sqrt

from time_benchmark import benchmark


@benchmark
def main():
    for b in range(1, 32):
        for a in range(1, b):
            c = a ** 2 + b ** 2
            if c == 1000:
                print(f"{a}: {a ** 2} + {b}: {b ** 2} = {c}")
                print(f"product from a b and c = {a * b * c ** 0.5}")


if __name__ == '__main__':
    main()
