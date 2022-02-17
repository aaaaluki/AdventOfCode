#!/usr/bin/env python
import sys
from simulation import Simulation

from numpy.core.numeric import ones_like

def part_one(lines):
    print('Part One')

    days = 80
    cycle = 6
    new_cycle = 8
    n = [int(i) for i in lines[0].split(',')]

    sim = Simulation(n, cycle, new_cycle)
    
    for i in range(days):
        sim.nextDay()
    
    print('    Day {:>3}: {:>12} fishes: {}'.format(i, sum(sim.m_state), sim.m_state))

    return

def part_two(lines):
    print('Part Two')

    days = 256
    cycle = 6
    new_cycle = 8
    n = [int(i) for i in lines[0].split(',')]

    sim = Simulation(n, cycle, new_cycle)
    
    for i in range(days):
        sim.nextDay()
    
    print('    Day {:>3}: {:>12} fishes: {}'.format(i, sum(sim.m_state), sim.m_state))

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