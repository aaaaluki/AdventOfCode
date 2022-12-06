#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')
    
    width = 4
    result = 0
    for line in lines:
        for i in range(len(line) - width):

            marker = line[i:i+width]
            if len(set(marker)) == width:
                result = i + width
                break

    print(f'Result: {result}')


def part_two(lines: List[str]):
    print('Part Two')

    width = 14
    result = 0
    for line in lines:
        for i in range(len(line) - width):

            marker = line[i:i+width]
            if len(set(marker)) == width:
                result = i + width
                break

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

