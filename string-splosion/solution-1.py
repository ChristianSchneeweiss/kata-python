from math import sqrt

from time_benchmark import benchmark


def string_splosion(word):
    splosion_word = [word[:i+1] for i in range(len(word))]
    return "".join(splosion_word)


@benchmark
def main():
    print(string_splosion("Code"))
    print(string_splosion('abc'))
    print(string_splosion('ab'))


if __name__ == '__main__':
    main()
