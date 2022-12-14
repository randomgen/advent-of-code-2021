import itertools
import sys


def convert(line):
    return line.strip()


def part1(data):
    print(list(data))
    return 0


def part2(data):
    print(list(data))
    return 0


def main(input_stream):
    data = map(convert, input_stream)
    data1, data2 = itertools.tee(data, 2)
    return part1(data1) or part2(data2)


if __name__ == '__main__':
    sys.exit(main(sys.stdin))
