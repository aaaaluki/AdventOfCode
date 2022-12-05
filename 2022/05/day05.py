#!/usr/bin/python3
import sys
from typing import List


def part_one(lines: List[str]):
    print('Part One')

    delta = 4
    n = len(lines[0])
    stacks = [[] for _ in range(int(n / delta) + 1)]
    for command_start, line in enumerate(lines):
        if lines[command_start + 1] == "":
            break
        
        for i, idx in enumerate(range(1, n, delta)):
            if line[idx] == " ":
                continue

            stacks[i] = [line[idx]] + stacks[i]
        
    for c in lines[command_start+2::]:
        parts = c.split(' ')
        quantity = int(parts[1])
        src = int(parts[3]) - 1
        dst = int(parts[5]) - 1

        crates = stacks[src][-quantity:][::-1] # Reverse crates since one at a time
        stacks[src] = stacks[src][:len(stacks[src]) - quantity]
        stacks[dst] = stacks[dst] + crates

    result = ''
    for s in stacks:
        print(s)
        result += s[-1]

    print(f'Result: {result}')

def part_two(lines: List[str]):
    print('Part Two')

    delta = 4
    n = len(lines[0])
    stacks = [[] for _ in range(int(n / delta) + 1)]
    for command_start, line in enumerate(lines):
        if lines[command_start + 1] == "":
            break
        
        for i, idx in enumerate(range(1, n, delta)):
            if line[idx] == " ":
                continue

            stacks[i] = [line[idx]] + stacks[i]
        
    for c in lines[command_start+2::]:
        parts = c.split(' ')
        quantity = int(parts[1])
        src = int(parts[3]) - 1
        dst = int(parts[5]) - 1

        crates = stacks[src][-quantity:] # We can move all the crates at the same time
        stacks[src] = stacks[src][:len(stacks[src]) - quantity]
        stacks[dst] = stacks[dst] + crates

    result = ''
    for s in stacks:
        print(s)
        result += s[-1]

    print(f'Result: {result}')


def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip('\n') for l in lines]

        part_one(lines)
        part_two(lines)


if __name__ == '__main__':
    main(sys.argv)
