#!/usr/bin/env python
import sys
import utils as ut

def part_one(lines):
    print('Part One')
    
    nums = [int(i) for i in lines[0].split(',')]
    hist = ut.histogram(nums)

    # Try binary search?¿
    i_left = 0
    i_right = len(hist)
    i_mid = (i_left + i_right) >> 1

    while True:

        i_mid = (i_left + i_right) >> 1
    
        cost_mid_low = ut.getCost(hist, i_mid - 1)
        cost_mid     = ut.getCost(hist, i_mid)
        cost_mid_upp = ut.getCost(hist, i_mid + 1)

        if cost_mid_low > cost_mid_upp:
            # Negative slope
            i_left = i_mid - 1

        elif cost_mid_upp > cost_mid_low:
            # Positive slope
            i_right = i_mid + 1
        
        if cost_mid < cost_mid_low and cost_mid < cost_mid_upp:
            break
    
    print('Result: pos = {}; cost = {}'.format(i_mid, cost_mid))

    return

def part_two(lines):
    print('Part Two')
    
    nums = [int(i) for i in lines[0].split(',')]
    hist = ut.histogram(nums)

    # Try binary search?¿
    i_left = 0
    i_right = len(hist)
    i_mid = (i_left + i_right) >> 1

    while True:

        i_mid = (i_left + i_right) >> 1
    
        cost_mid_low = ut.getCost2(hist, i_mid - 1)
        cost_mid     = ut.getCost2(hist, i_mid)
        cost_mid_upp = ut.getCost2(hist, i_mid + 1)

        if cost_mid_low > cost_mid_upp:
            # Negative slope
            i_left = i_mid - 1

        elif cost_mid_upp > cost_mid_low:
            # Positive slope
            i_right = i_mid + 1
        
        if cost_mid < cost_mid_low and cost_mid < cost_mid_upp:
            break
    
    print('Result: pos = {}; cost = {}'.format(i_mid, cost_mid))

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