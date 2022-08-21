from typing import Any, Callable, Iterable, Tuple

import itertools
import sys


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def __iter__(self) -> Iterable[Point]:
        step = Point(cmp(self.start.x, self.end.x),
                     cmp(self.start.y, self.end.y))
        current = self.start
        while True:
            yield current
            if current == self.end:
                break
            current = Point(current.x + step.x, current.y + step.y)


def cmp(a: int, b: int) -> int:
    return 1 if a < b else -1 if a > b else 0


def convert(line: str) -> Tuple[Point, Point]:
    x1, y1, x2, y2 = map(int, line.strip().replace(' -> ', ',').split(','))
    return Point(x1, y1), Point(x2, y2)


def is_horizontal(line: Line) -> bool:
    return line.start.y == line.end.y


def is_vertical(line: Line) -> bool:
    return line.start.x == line.end.x


def is_diagonal(line: Line) -> bool:
    return not is_horizontal(line) and not is_vertical(line)


def count_if(func: Callable[[Any], bool], iterable: Iterable[Any]) -> int:
    count = 0
    for x in iterable:
        if func(x):
            count += 1
    return count


def part1(data, ignore_diagonal=True):
    GRID = Point(1000, 1000)
    diagram = [[0 for y in range(GRID.y)] for x in range(GRID.x)]
    lines = [Line(start, end) for start, end in data]
    if ignore_diagonal:
        lines = [line for line in lines if not is_diagonal(line)]
    for line in lines:
        for point in line:
            diagram[point.x][point.y] += 1
    flatten = [count for rows in diagram for count in rows]
    count = count_if(lambda x: x > 1, flatten)
    print(count)
    return 0


def part2(data):
    return part1(data, ignore_diagonal=False)


def main(input_stream):
    data = map(convert, input_stream)
    data1, data2 = itertools.tee(data, 2)
    return part1(data1) or part2(data2)


if __name__ == '__main__':
    sys.exit(main(sys.stdin))
