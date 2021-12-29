import fileinput
import itertools
import sys


def convert(line):
    return int(line.strip())


def part1(depths):
    count = 0
    previous = None
    for current in depths:
        if previous and current > previous:
            count += 1
        previous = current
    print(count)
    return 0


def part2(depths):
    count = 0
    previous = None
    depths = list(depths)
    for i in range(len(depths)):
        window = depths[i:i+3]
        if len(window) < 3:
            break
        if previous and sum(window) > previous:
            count += 1
        previous = sum(window)
    print(count)
    return 0


def main():
    data = map(convert, fileinput.input())
    data1, data2 = itertools.tee(data, 2)
    return part1(data1) or part2(data2)


if __name__ == '__main__':
    sys.exit(main())
