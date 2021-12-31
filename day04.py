from functools import partial
from itertools import chain
from operator import eq, lt
import sys


class Bingo:
    class Mark:
        NONE = 0
        DRAWN = -1
        WON = -2

    LINE_SIZE = 5
    BOARD_SIZE = LINE_SIZE * LINE_SIZE

    unmarked = partial(lt, Mark.NONE)
    is_line_complete = partial(eq, [Mark.DRAWN] * LINE_SIZE)

    def __init__(self, numbers):
        self.numbers = numbers

    def board(self, i):
        return self.numbers[self.board_slice(i)]

    def board_slice(self, i):
        return slice(i * self.BOARD_SIZE, i * self.BOARD_SIZE + self.BOARD_SIZE)

    def columns(self):
        for i in range(0, len(self.numbers), self.BOARD_SIZE):
            for j in range(i, i + self.LINE_SIZE):
                yield self.numbers[j:j + self.BOARD_SIZE:self.LINE_SIZE]

    def mark(self, draw):
        for i, v in enumerate(self.numbers):
            if v == draw:
                self.numbers[i] = self.Mark.DRAWN

    def remove_board(self, i):
        self.numbers[self.board_slice(i)] = [self.Mark.WON] * self.BOARD_SIZE

    def rows(self):
        for i in range(0, len(self.numbers), self.LINE_SIZE):
            yield self.numbers[i:i + self.LINE_SIZE]

    def winners(self):
        completed_rows = [i for i, line in enumerate(self.rows()) if self.is_line_complete(line)]
        completed_cols = [i for i, line in enumerate(self.columns()) if self.is_line_complete(line)]
        completed = chain(completed_rows, completed_cols)
        boards = map(lambda i: int(i / self.LINE_SIZE), completed)
        return set(boards)


def convert_draws(line):
    return list(map(int, line.strip().split(',')))


def convert_board_line(line):
    return list(map(int, line.strip().split()))


def load(input_stream):
    draws = convert_draws(next(input_stream))
    boards = []
    for line in input_stream:
        if not line.isspace():
            boards.extend(convert_board_line(line))
    return draws, boards


def part1(scores):
    print(scores[0])
    return 0


def part2(scores):
    print(scores[-1])
    return 0


def main(input_stream):
    draws, boards = load(input_stream)
    bingo = Bingo(boards)
    scores = []
    for draw in draws:
        bingo.mark(draw)
        for winner in bingo.winners():
            unmarked = filter(Bingo.unmarked, bingo.board(winner))
            scores.append(sum(unmarked) * draw)
            bingo.remove_board(winner)
    return part1(scores) or part2(scores)


if __name__ == '__main__':
    sys.exit(main(sys.stdin))
