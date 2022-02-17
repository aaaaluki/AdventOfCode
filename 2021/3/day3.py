#!/usr/bin/env python
import numpy as np
import sys

def part_one(lines):
    print('Part One')

    gamma = 0
    epsilon = 0
    
    N = len(lines[0].strip())
    count = np.array([0]*N)

    for l in lines:
        l = np.array([int(i) for i in l.strip()])
    
        # From 0:1 range to -1:1 range
        l = 2*l - 1
    
        count += l

    # Get the binary value as an array
    # -1:1 range to 0:1 range
    count = (np.sign(count) + 1) >> 1

    # Transform the binary array to the decmal value
    gamma = 0
    for i in range(N):
        gamma += count[i]*(1 << N-1 - i)

    # Get the value as an unsigned int
    epsilon = ~gamma + (1 << N)

    print('\tGamma = {} ({})'.format(gamma, bin(gamma)))
    print('\tEpsilon = {} ({})'.format(epsilon, bin(epsilon)))
    print('\tPower consumption = {}'.format(gamma*epsilon))

    return

def part_two(lines):
    print('Part Two')

    N = len(lines[0].strip())

    # Calculate oxygen generator rating
    remaining = lines
    for i in range(N):
        one_count = 0
        zero_count = 0
        ones = []
        zeros = []

        for l in remaining:
            if l[i] == '1':
                one_count += 1
                ones.append(l)
            else:
                zero_count += 1
                zeros.append(l)

        if one_count >= zero_count:
            remaining = ones
        else:
            remaining = zeros
        
        if len(remaining) == 1:
            break
    oxygen = remaining[0].strip()

    # Calculate CO2 scrubber rating
    remaining = lines
    for i in range(N):
        one_count = 0
        zero_count = 0
        ones = []
        zeros = []

        for l in remaining:
            if l[i] == '1':
                one_count += 1
                ones.append(l)
            else:
                zero_count += 1
                zeros.append(l)

        if one_count >= zero_count:
            remaining = zeros
        else:
            remaining = ones
        
        if len(remaining) == 1:
            break
    co2 = remaining[0].strip()

    oxygen = int(oxygen, base=2)
    co2 =  int(co2, base=2)


    print('\tO2 = {} ({})'.format(oxygen, bin(oxygen)))
    print('\tCO2 = {} ({})'.format(co2, bin(co2)))
    print('\tLife support = {}'.format(oxygen*co2))

    return

def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()

        part_one(lines)
        part_two(lines)


if __name__ == '__main__':
    main(sys.argv)