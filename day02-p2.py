import fileinput
import sys


CMD_DIRECTION = 0
CMD_DISTANCE = 1


def convert(line):
    parts = line.split()
    return parts[CMD_DIRECTION], int(parts[CMD_DISTANCE])


def main():
    horizontal_position = 0
    depth = 0
    aim = 0
    commands = map(convert, fileinput.input())
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


if __name__ == '__main__':
    sys.exit(main())
