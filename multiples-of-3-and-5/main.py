def is_multiple_of_3_and_5(num) -> bool:
    return num % 15 == 0


def main():
    sum = calculate_sum()
    print(f"sum = {sum}")


def calculate_sum():
    sum = 0
    for num in range(0, 1000):
        if is_multiple_of_3_and_5(num):
            sum += num
    return sum


if __name__ == '__main__':
    main()
