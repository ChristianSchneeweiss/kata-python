from time_benchmark import benchmark


@benchmark
def main():
    palindromes = {product: tuple([a, b]) for a, b, product in gen_3_digit_product() if is_palindrome(product)}
    # for key, value in palindromes.items():
    #     print(f"{value[0]} * {value[1]} = {key}")
        
    max_palindrome = max(palindromes.items())
    print(f"max palindrome is {max_palindrome[0]} = {max_palindrome[1][0]} * {max_palindrome[1][1]}")


def is_palindrome(num: int) -> bool:
    return str(num)[::-1] == str(num)


def gen_3_digit_product():
    for i in range(100, 1000):
        for j in range(i, 1000):
            yield i, j, i * j


if __name__ == '__main__':
    main()
