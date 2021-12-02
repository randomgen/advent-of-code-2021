import fileinput
import sys


def convert(line):
    return int(line.strip())


def main():
    count = 0
    previous = None
    lines = list(map(convert, fileinput.input()))
    for i in range(len(lines)):
        window = lines[i:i+3]
        if len(window) < 3:
            break
        if previous and sum(window) > previous:
            count += 1
        previous = sum(window)
    print(count)
    return 0


if __name__ == '__main__':
    sys.exit(main())
