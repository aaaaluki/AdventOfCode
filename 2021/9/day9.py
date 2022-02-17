#!/usr/bin/env python
import sys
import utils

def part_one(lines):
    print('Part One')

    rows = len(lines)
    cols = len(lines[0])

    # Construct matrix
    mat = [[]]*rows
    for i in range(rows):
        mat[i] = [int(c) for c in lines[i]]

    mins = utils.find_local_minima(mat)

    risk = 0
    for m in mins:
        risk += mat[m[0]][m[1]] + 1

    print('Risk level: {}'.format(risk))

    return

def part_two(lines):
    print('Part Two')

    rows = len(lines)
    cols = len(lines[0])

    # Construct matrix
    mat = [[]]*rows
    for i in range(rows):
        mat[i] = [int(c) for c in lines[i]]

    # Find local minima
    mins = utils.find_local_minima(mat)

    # Convert the matrix to 'binary' form:
    #   + 0 -> numbers from 0 to 8
    #   + 1 -> 9
    binary_mat = [[]]*rows
    for r in range(rows):
        arr = []
        for c in range(cols):
            if mat[r][c] == 9:
                arr.append(1)
                print('#', end='')
            else:
                arr.append(0)
                print('.', end='')
        
        binary_mat[r] = arr
        print()

    # Find the basin sizes
    basin_sizes = []
    for node in mins:
        basin_sizes.append(utils.flood_fill(binary_mat, node))

    # Sort basin sizes in descending order
    basin_sizes.sort(reverse=True)

    # Get the sum of the largest ones
    basin_sum = 1
    for i in range(3):
        basin_sum *= basin_sizes[i]

    print('Result: {}'.format(basin_sum))

    return

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