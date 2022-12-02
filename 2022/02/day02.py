#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    result = 0
    for line in lines:
        plays = line.split(' ')

        if plays[1] == 'X': # Rock
            result += 1
            if plays[0] == 'A': # Rock
                result += 3
            elif plays[0] == 'B': # Paper
                result += 0
            else: # Scissors
                result += 6
        elif plays[1] == 'Y': # Paper
            result += 2
            if plays[0] == 'A': # Rock
                result += 6
            elif plays[0] == 'B': # Paper
                result += 3
            else: # Scissors
                result += 0
        else: # Scissors
            result += 3
            if plays[0] == 'A': # Rock
                result += 0
            elif plays[0] == 'B': # Paper
                result += 6
            else: # Scissors
                result += 3

    print(f'Result: {result}')


def part_two(lines: List[str]):
    print('Part Two')

    result = 0
    for line in lines:
        plays = line.split(' ')
        if plays[1] == 'X': # Lose
            result += 0
            if plays[0] == 'A': # Rock / Scissors
                result += 3
            elif plays[0] == 'B': # Paper / Rock
                result += 1
            else: # Scissors / Paper
                result += 2
        elif plays[1] == 'Y': # Draw
            result += 3
            if plays[0] == 'A': # Rock / Rock
                result += 1
            elif plays[0] == 'B': # Paper / Paper
                result += 2
            else: # Scissors/ Scissors
                result += 3
        else: # Win
            result += 6
            if plays[0] == 'A': # Rock / Paper
                result += 2
            elif plays[0] == 'B': # Paper / Scissors
                result += 3
            else: # Scissors / Rock
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
