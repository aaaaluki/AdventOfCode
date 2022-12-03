#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    common_items = []
    for line in lines:
        comp1, comp2 = line[:len(line)//2], line[len(line)//2:]

        common_items.append(''.join(set(comp1).intersection(comp2)))

    result = 0
    for item in common_items:
        foo = ord(item) - 0x60
        foo = foo if (foo > 0) else (foo + 29*2)
        result += foo

    print(f'Result: {result}')


def part_two(lines: List[str]):
    print('Part Two')

    common_items = []
    for idx in range(0, len(lines), 3):

        common_items.append(''.join(set.intersection(*[set(l) for l in lines[idx:idx + 3]])))

    result = 0
    for item in common_items:
        foo = ord(item) - 0x60
        foo = foo if (foo > 0) else (foo + 29*2)
        result += foo

    print(f'Result: {result}')


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
