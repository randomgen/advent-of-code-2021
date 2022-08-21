from typing import Any, Callable, Iterable, Tuple

import itertools
import sys


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def __iter__(self) -> Iterable[Point]:
        step = Point(1 if self.end.x - self.start.x >= 0 else -1,
                     1 if self.end.y - self.start.y >= 0 else -1)
        for x in range(self.start.x, self.end.x + step.x, step.x):
            for y in range(self.start.y, self.end.y + step.y, step.y):
                yield Point(x, y)


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


def part1(data):
    GRID = Point(1000, 1000)
    diagram = [[0 for y in range(GRID.y)] for x in range(GRID.x)]
    lines = [Line(start, end) for start, end in data]
    lines = [line for line in lines if not is_diagonal(line)]
    for line in lines:
        for point in line:
            diagram[point.x][point.y] += 1
    flatten = [count for rows in diagram for count in rows]
    count = count_if(lambda x: x > 1, flatten)
    print(count)
    return 0


def part2(data):
    return 0


def main(input_stream):
    data = map(convert, input_stream)
    data1, data2 = itertools.tee(data, 2)
    return part1(data1) or part2(data2)


if __name__ == '__main__':
    sys.exit(main(sys.stdin))
