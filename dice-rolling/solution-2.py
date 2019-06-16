import math

import numpy as np

from time_benchmark import benchmark


def get_dice_roll():
    return math.floor(np.random.rand() * 6) + 1


@benchmark
def main():
    print(get_dice_roll())
    print(get_dice_roll())
    print(get_dice_roll())
    print(get_dice_roll())


if __name__ == '__main__':
    main()
