from typing import Optional

import itertools
import sys


class Lanternfish:
    def __init__(self, timer: int) -> None:
        self.timer = timer

    def __str__(self) -> str:
        return str(self.timer)

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Lanternfish(8)


def convert(line):
    return map(int, line.strip().split(','))


def part1(data):
    population = list(map(Lanternfish, data))
    for _ in range(80):
        children = []
        for fish in population:
            child = fish.tick()
            if child:
                children.append(child)
        population.extend(children)
    print(len(population))
    return 0


def part2(data):
    return 0


def main(input_stream):
    data = map(convert, input_stream)
    data1, data2 = itertools.tee(data, 2)
    return part1(next(data1)) or part2(next(data2))


if __name__ == '__main__':
    sys.exit(main(sys.stdin))
