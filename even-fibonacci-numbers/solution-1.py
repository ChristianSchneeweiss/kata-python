from time_benchmark import benchmark


def generate_fibonacci_up_to(num):
    x = 1
    y = 1
    while y < num:
        yield y
        h = y
        y += x
        x = h


@benchmark
def main():
    even_sum = sum({num for num in generate_fibonacci_up_to(4_000_000) if num % 2 == 0})
    print(f"Sum of even fibonacci numbers up to 4M is {even_sum}\n")


if __name__ == '__main__':
    main()
