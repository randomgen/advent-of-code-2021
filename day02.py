import collections
import fileinput
import itertools
import sys


CMD_DIRECTION = 0
CMD_DISTANCE = 1


def convert(line):
    parts = line.split()
    return parts[CMD_DIRECTION], int(parts[CMD_DISTANCE])


def part1(commands):
    acc = collections.defaultdict(int)
    for command in commands:
        acc[command[CMD_DIRECTION]] += command[CMD_DISTANCE]
    print(acc['forward'] * (acc['down'] - acc['up']))
    return 0


def part2(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        if command[CMD_DIRECTION] == 'forward':
            horizontal_position += command[CMD_DISTANCE]
            depth += aim * command[CMD_DISTANCE]
        elif command[CMD_DIRECTION] == 'up':
            aim -= command[CMD_DISTANCE]
        elif command[CMD_DIRECTION] == 'down':
            aim += command[CMD_DISTANCE]
    print(horizontal_position * depth)
    return 0


def main():
    data = map(convert, fileinput.input())
    data1, data2 = itertools.tee(data, 2)
    return part1(data1) or part2(data2)


if __name__ == '__main__':
    sys.exit(main())
