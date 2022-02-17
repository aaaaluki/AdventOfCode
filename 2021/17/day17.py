#!/usr/bin/env python
import sys
import utils
from typing import List
from progress.bar import Bar

def parts(lines:List[str]):

    for l in lines:
        _, target_str = l.split(': ')

        # Target bound calculation
        x, y = target_str.split(', ')
        x = x[2:].split('..')
        x = sorted([int(n) for n in x])
        y = y[2:].split('..')
        y = sorted([int(n) for n in y])

        target = ((x[0], y[0]), (x[1], y[1]))

        # Result variables
        max_y = 0
        vel_opt = None

        vels_reachable = 0


        Nx = target[1][0]
        Ny_min = target[0][1]
        Ny_max = abs(Ny_min)
        bar = Bar('Remaining:', max=Nx, suffix='%(percent)d%%')

        print('Brute force limits: (0 -> {}, {} -> {})'.format(Nx, Ny_min, Ny_max))

        for i in range(Nx + 1):
            for j in range(Ny_min - 1, Ny_max):
                vel = (i, j)
                probe = utils.Probe(vel, target)

                below = False
                while not below:
                    below, reached = probe.step()
                
                if reached:
                    vels_reachable += 1

                    if probe.m_max_y > max_y:
                        max_y = probe.m_max_y
                        vel_opt = vel
            
            bar.next()


        bar.finish()

        print('Max y reached: {};'.format(max_y))
        print('Initial velocity: {};'.format(vel_opt))
        print('Distinct v0 count: {};'.format(vels_reachable))

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

        parts(lines)


if __name__ == '__main__':
    main(sys.argv)
