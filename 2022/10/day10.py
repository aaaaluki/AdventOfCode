#!/usr/bin/python3
import sys
from typing import List


WAIT_TIME = {'addx': 2, 'noop': 1}
RESULT_CYCLES = [20, 60, 100, 140, 180, 220]
SCREEN_WIDTH = 40

def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    print('Part One')

    result_p1 = []
    result_p2 = ""

    areg = 0
    xreg = 1
    cycle_num = -1  # Don't know, just works
    twait = 0
    pc = 0

    while pc <= len(lines):
        cycle_num += 1
        print(f'[0x{cycle_num:04x}] areg:{areg:03d} xreg:{xreg:03d}')

        if cycle_num in RESULT_CYCLES:
            result_p1.append(cycle_num*xreg)

        if cycle_num > 0: # Skip first cycle, don't know why, just works
            if (cycle_num - 1) % SCREEN_WIDTH in range(xreg - 1, xreg + 2):
                result_p2 += '#'
            else:
                result_p2 += '.'

        if twait > 0:
            twait -= 1
            continue

        xreg += areg

        if pc == len(lines):
            break

        cmd = lines[pc].split(' ')
        if cmd[0] == 'noop':
            twait = 0
            areg = 0
        elif cmd[0] == 'addx':
            twait = 1
            areg = int(cmd[1])

        pc += 1

    print(f'Result: {sum(result_p1)}')

    print('Part Two')
    for i in range(0, len(result_p2), SCREEN_WIDTH):
        print(result_p2[i:i+SCREEN_WIDTH])



if __name__ == '__main__':
    main(sys.argv)
