#!/usr/bin/env python
import sys

def part_one(lines):
    prev = lines[0]
    count = 0
    for i in range(1, len(lines)):
        if lines[i] > prev:
            count += 1

        prev = lines[i]

    print(f'Part One: Count = {count}')
    return

def part_two(lines, N):
    count = 0

    prev = sum(lines[0:N])
    for i in range(1, len(lines) - N + 1):
        now = sum(lines[i:i + N])
        if now > prev:
            count += 1
        
        prev = now
            
    print(f'Part Two: Count = {count}')
    return

def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = [int(l) for l in f.readlines()]

        part_one(lines)
        part_two(lines, 3)


if __name__ == '__main__':
    main(sys.argv)