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


def find_rating(report, bit, func):
    if len(report) == 0:
        return None
    
    if len(report) == 1:
        return int(to_binary_str(report[0]), base=2)

    counters = count_bits(report)
    bit_criteria = list(map(func(len(report)), counters))
    filtered = list(filter(lambda x: x[bit] == bit_criteria[bit], report))
    return find_rating(filtered, bit + 1, func)


def most_common(n):
    return lambda x: int(x >= (n / 2))


def least_common(n):
    return lambda x: int(x < (n / 2))


def to_binary_str(lst):
    return ''.join(map(str, lst))


def main():
    report = list(map(convert, fileinput.input()))
    oxygen_generator_rating = find_rating(report, 0, most_common)
    co2_scrubber_rating = find_rating(report, 0, least_common)
    print(oxygen_generator_rating * co2_scrubber_rating)
    return 0


if __name__ == '__main__':
    sys.exit(main())
