import fileinput
import sys


def convert(line):
    return int(line.strip())


def main():
    count = 0
    previous = None
    lines = map(convert, fileinput.input())
    for current in lines:
        if previous and current > previous:
            count += 1
        previous = current
    print(count)
    return 0


if __name__ == '__main__':
    sys.exit(main())
