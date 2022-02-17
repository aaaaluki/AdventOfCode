#!/usr/bin/env python
import sys
from simulation import Simulation

def part_one(lines):
    print('Part One')

    steps = 100

    state = []
    for l in lines:
        state.append([int(n) for n in l])

    sim = Simulation(state, False)

    for i in range(steps):
        sim.nextStep()

    print('Number of flashes: {}'.format(sim.m_flash_count))

    return

def part_two(lines):
    print('Part Two')

    state = []
    for l in lines:
        state.append([int(n) for n in l])

    sim = Simulation(state, False)

    while sim.m_state.sum() != 0:
        sim.nextStep()

    print('Number of steps: {}'.format(sim.m_step))

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