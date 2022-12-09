#!/usr/bin/python3
import sys
from typing import List

import numpy as np


def move_from_delta(delta):
    # Basic mapping, these can be rotated by 90 deg (total of 16 moves)
    # delta -> move
    # 0 + 0j -> 0 + 0j
    # 0 + 1j -> 0 + 0j
    # 1 + 1j -> 0 + 0j
    # 0 + 2j -> 0 + 1j
    # 1 + 2j -> 1 + 1j
    angle = (np.angle(delta, deg=True) + 360) % 360
    norm = np.absolute(delta)

    if norm < 2:
        return 0 + 0j

    if int(angle) in [0, 90, 180, 270]:
        angle = int(angle)
        return np.round(np.exp(1j*np.deg2rad(angle)))

    quadrant_angles = np.array([45, 135, 225, 315])
    quadrant = np.argmin(np.abs(quadrant_angles - angle*np.ones_like(quadrant_angles)))

    return np.round(np.exp(1j*(quadrant*np.pi/2 + np.pi/4)))


def part_one(lines: List[str]):
    print('Part One')

    head = 0 + 0j
    tail = 0 + 0j

    visited_positions = set()

    for line in lines:
        cmd, length = line.split(' ')
        length = int(length)
        if cmd == 'R':
            vec =  1 + 0j
        elif cmd == 'U':

            vec =  0 + 1j
        elif cmd == 'L':
            vec = -1 + 0j
        else: # D
            vec =  0 - 1j

        for i in range(length):
            head += vec
            delta = head - tail

            move = move_from_delta(delta)
            tail += move

            visited_positions.add(tail)

    print(f'Result: {len(visited_positions)}')


def part_two(lines: List[str]):
    print('Part Two')

    tail_number = 9
    knots = [0 + 0j for i in range(tail_number + 1)] # Head + tails

    visited_positions = set()

    for line in lines:
        cmd, length = line.split(' ')
        length = int(length)
        if cmd == 'R':
            vec =  1 + 0j
        elif cmd == 'U':

            vec =  0 + 1j
        elif cmd == 'L':
            vec = -1 + 0j
        else: # D
            vec =  0 - 1j

        for i in range(length):
            knots[0] += vec

            # Calc deltas
            for i in range(tail_number):
                delta = knots[i] - knots[i + 1]
                move = move_from_delta(delta)
                knots[i + 1] += move

            visited_positions.add(knots[tail_number])

    print(f'Result: {len(visited_positions)}')


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
