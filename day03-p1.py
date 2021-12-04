import fileinput
import sys


def convert(line):
    return [int(c) for c in line.strip()]


def count_bits(report):
    counters = [0] * len(report[0])
    for line in report:
        for i, v in enumerate(line):
            counters[i] += v
    return counters


def compute_rate(counters, func):
    rate = map(func, counters)
    return int(to_binary_str(rate), base=2)


def most_common(n):
    return lambda x: int(x >= (n / 2))


def least_common(n):
    return lambda x: int(x < (n / 2))


def to_binary_str(lst):
    return ''.join(map(str, lst))


def main():
    report = list(map(convert, fileinput.input()))
    counters = count_bits(report)
    gamma_rate = compute_rate(counters, most_common(len(report)))
    epsilon_rate = compute_rate(counters, least_common(len(report)))
    print(gamma_rate * epsilon_rate)
    return 0


if __name__ == '__main__':
    sys.exit(main())
