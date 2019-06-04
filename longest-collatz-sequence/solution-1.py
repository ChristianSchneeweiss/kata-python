from time_benchmark import benchmark


def gen_collatz(num):
    while num != 1:
        yield num
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
    yield 1


@benchmark
def main():
    longest = {"len": 0, "num": 0}
    for i in range(1, 1_000_000):
        l = list(gen_collatz(i))
        if longest["len"] < len(l):
            longest["len"] = len(l)
            longest["num"] = i
    
    print(f"longest is {longest['num']} with {longest['len']} iterations")


if __name__ == '__main__':
    main()
