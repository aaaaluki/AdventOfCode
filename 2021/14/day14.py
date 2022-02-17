#!/usr/bin/env python
from os import stat
import sys
import utils
from typing import List
from collections import Counter, UserList


def part_one(lines:List[str]):
    print('Part One')

    steps = 10
    state = lines[0]
    rules = {}

    for i in range(2, len(lines)):
        k, v = lines[i].split(' -> ')

        rules[k] = v
    
    for i in range(1, steps + 1):
        state = utils.step(state, rules)

    c = Counter(state)
    vals = c.most_common()

    print('Result = {}'.format(vals[0][1] - vals[-1][1]))

    return

def part_two(lines:List[str]):
    print('Part Two')

    steps = 40
    state = lines[0]
    rules = {}

    for i in range(2, len(lines)):
        k, v = lines[i].split(' -> ')

        rules[k] = v
    
    histo = utils.pair_histogram(state)

    for i in range(1, steps + 1):
        histo = utils.fast_step(histo, rules)

    count = utils.count_elements(histo)
    vals = sorted(list(count.values()), reverse=True)
    
    print('Result = {}'.format(vals[0] - vals[-1]))

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