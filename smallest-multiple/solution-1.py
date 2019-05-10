from time_benchmark import benchmark


def is_dividable_up_to_20(num: int) -> bool:
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True


def gen_number():
    num = 20
    while True:
        yield num
        num += 20


@benchmark
def main():
    for num in gen_number():
        if is_dividable_up_to_20(num):
            print(num)
            break


if __name__ == '__main__':
    main()
