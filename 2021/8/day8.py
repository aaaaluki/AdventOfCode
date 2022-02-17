#!/usr/bin/env python
import sys
import utils as ut

def part_one(lines):
    print('Part One')

    # Corresponding to: 1, 7 ,4, 8
    unique_lengths = [2, 3, 4, 7]

    count = 0
    for l in lines:
        vals = l.split('|')
        unique = vals[0].strip()
        output = vals[1].strip()

        for s in output.split(' '):
            if len(s) in unique_lengths:
                count += 1

    print('Result = {}'.format(count))

    return

def part_two(lines):
    print('Part Two')

    count = 0
    for l in lines:
        tmp = l.split('|')
        inp = tmp[0]
        out = tmp[1]

        key = ut.getKey(inp)
        num = ut.getNum(out, key)

        count += num

        #print('Key = {}; Number = {:04d};'.format(key, num))
    
    print('Result = {}'.format(count))

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