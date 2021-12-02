import collections
import fileinput
import sys


CMD_DIRECTION = 0
CMD_DISTANCE = 1


def convert(line):
    parts = line.split()
    return parts[CMD_DIRECTION], int(parts[CMD_DISTANCE])


def main():
    acc = collections.defaultdict(int)
    commands = map(convert, fileinput.input())
    for command in commands:
        acc[command[CMD_DIRECTION]] += command[CMD_DISTANCE]
    print(acc['forward'] * (acc['down'] - acc['up']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
