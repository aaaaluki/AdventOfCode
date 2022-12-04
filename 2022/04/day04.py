#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    result = 0
    for line in lines:
        elf1, elf2 = line.split(',')

        comps = elf1.split('-')
        elf1 = set(range(int(comps[0]), int(comps[1]) + 1))
        comps = elf2.split('-')
        elf2 = set(range(int(comps[0]), int(comps[1]) + 1))

        if elf1.issubset(elf2) or elf2.issubset(elf1):
            result += 1

    print(f'Result: {result}')


def part_two(lines: List[str]):
    print('Part Two')

    result = 0
    for line in lines:
        elf1, elf2 = line.split(',')

        comps = elf1.split('-')
        elf1 = set(range(int(comps[0]), int(comps[1]) + 1))
        comps = elf2.split('-')
        elf2 = set(range(int(comps[0]), int(comps[1]) + 1))

        if len(elf1.intersection(elf2)) != 0:
            result += 1

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
