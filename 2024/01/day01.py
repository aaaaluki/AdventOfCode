#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')
    locs = [[], []]
    for l in lines:
        a, b = l.split("   ")
        locs[0].append(int(a))
        locs[1].append(int(b))

    for l in locs:
        l.sort()

    r1 = 0
    for a, b in zip(*locs):
        r1 += abs(a - b)
    print(r1)

    print('Part Two')

    r2 = 0
    freqs = dict()
    for e in locs[1]:
        if e not in freqs:
            freqs[e] = 0
        freqs[e] += 1

    for v in locs[0]:
        r2 += v*freqs.get(v, 0)
    print(r2)

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


if __name__ == '__main__':
    main(sys.argv)
