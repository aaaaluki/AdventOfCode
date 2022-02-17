#!/usr/bin/env python
import sys
import utils
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    prev = utils.reduce(lines[0])
    for i in range(1, len(lines)):
        a = lines[i].replace(' ', '')
        if lines[i] == '':
            continue

        a = utils.add(prev, a)
        if utils.VERBOSE:
            print('Reducing:\t\t{}'.format(a))

        a = utils.reduce(a)
        prev = a

    print('Final number: {}'.format(a))
    print('Final magnitude: {}'.format(utils.magnitude(a)))


def part_two(lines: List[str]):
    print('Part Two')

    max_sum = 0
    pair = None
    for l1 in lines:
        for l2 in lines:
            snail_sum = utils.magnitude(utils.reduce(utils.add(l1, l2)))

            if snail_sum > max_sum:
                max_sum = snail_sum
                pair = (l1, l2)

    print('Pair: {} + {}'.format(pair[0], pair[1]))
    print('Final magnitude: {}'.format(max_sum))


def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        part_one(lines)
        part_two(lines)


if __name__ == '__main__':
    main(sys.argv)
