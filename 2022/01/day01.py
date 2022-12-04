#!/usr/bin/python3
import sys
from typing import List


def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    print('Part One ' + '#'*41)
    calories = [0]

    for line in lines:
        if line != '':
            calories[-1] += int(line)
        else:
            calories.append(0)

    calories.sort(reverse=True)
    print(f'Max calories: {calories[0]}')

    print('Part Two ' + '#'*41)
    print(f'Max calories: {sum(calories[:3])}')


if __name__ == '__main__':
    main(sys.argv)
