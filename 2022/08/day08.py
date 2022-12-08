#!/usr/bin/python3
import numpy as np
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    width = len(lines[0])
    height = len(lines)

    result = 0
    forest = np.zeros((width, height), dtype=int)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            forest[row][col] = int(char)

    result += 2*width
    result += 2*(height - 2)

    print(forest)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            tree = forest[row][col]

            visible_count = 0
            # Trees to the west
            visible = True
            for i in range(col):
                if forest[row][i] >= tree:
                    visible = False
                    break
            if visible:
                visible_count += 1
                
            # Trees to the east
            visible = True
            for i in range(width - 1, col, -1):
                if forest[row][i] >= tree:
                    visible = False
                    break
            if visible:
                visible_count += 1
                
            # Trees to the north
            visible = True
            for i in range(row):
                if forest[i][col] >= tree:
                    visible = False
                    break
            if visible:
                visible_count += 1
                
            # Trees to the south
            visible = True
            for i in range(height - 1, row, -1):
                if forest[i][col] >= tree:
                    visible = False
                    break
            if visible:
                visible_count += 1

            if visible_count != 0:
                result += 1

    print(f'Result: {result}')

def part_two(lines: List[str]):
    print('Part Two')

    width = len(lines[0])
    height = len(lines)

    result = 0
    forest = np.zeros((width, height), dtype=int)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            forest[row][col] = int(char)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            tree = forest[row][col]
            scenic_view = np.zeros(4, dtype=int)

            # Trees to the west
            if col != 0:
                max_height = forest[row][col - 1]
                for i in range(col - 1, -1, -1):
                    # if forest[row][i] >= max_height and max_height <= tree:
                    if forest[row][i] >= tree:
                        scenic_view[3] += 1
                        break
                    if forest[row][i] <= tree:
                        max_height = forest[row][i]
                        scenic_view[3] += 1
                
            # Trees to the east
            if col != width - 1:
                max_height = forest[row][col + 1]
                for i in range(col + 1, width):
                    # if forest[row][i] >= max_height and max_height <= tree:
                    if forest[row][i] >= tree:
                        scenic_view[1] += 1
                        break
                    if forest[row][i] <= tree:
                        max_height = forest[row][i]
                        scenic_view[1] += 1
                
            # Trees to the north
            if row != 0:
                max_height = forest[row - 1][col]
                for i in range(row - 1, -1, -1):
                    # if forest[i][col] >= max_height and max_height <= tree:
                    if forest[i][col] >= tree:
                        scenic_view[0] += 1
                        break
                    if forest[i][col] <= tree:
                        max_height = forest[i][col]
                        scenic_view[0] += 1
                
            # Trees to the south
            if row != height - 1:
                max_height = forest[row + 1][col]
                for i in range(row + 1, height):
                    # if forest[i][col] >= max_height and max_height <= tree:
                    if forest[i][col] >= tree:
                        scenic_view[2] += 1
                        break
                    if forest[i][col] <= tree:
                        max_height = forest[i][col]
                        scenic_view[2] += 1
                
            scenic_view_result = np.prod(scenic_view)
            # print(f'({row},{col}) {tree}: {scenic_view} -> {scenic_view_result}')
            if scenic_view_result > result:
                print(f'({row},{col}) {tree}: {scenic_view} -> {scenic_view_result}')
                result = scenic_view_result

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
