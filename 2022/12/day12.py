#!/usr/bin/python3
import sys
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import art3d
from matplotlib.patches import Circle


SHIFT = 0x61 # ASCII for a


def plot_mountain(mountain, start, finish):
    """
    LEGO plot
    """
    # https://stackoverflow.com/a/51624201
    mountain = np.array(mountain, dtype=np.int8)

    _x = np.arange(mountain.shape[1])
    _y = np.arange(mountain.shape[0])
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    z = np.zeros_like(x)

    dx = dy = 1
    dz = mountain.ravel()

    cmap = cm.get_cmap('coolwarm_r') # Get desired colormap - you can change this!
    max_height = np.max(dz)   # get range of colorbars so we can normalize
    min_height = np.min(dz)
    rgba = [cmap((k-min_height)/max_height) for k in dz]

    fig = plt.figure()          #create a canvas, tell matplotlib it's 3d
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(x, y, z, dx, dy, dz, color=rgba, zsort='average')
    ax.set_title('Mountain')

    # Mark start and finish
    psize = 0.5
    pec = 'k'
    pfc = 'k'
    pstart = Circle(start, psize, ec=pec, fc=pfc)
    ax.add_patch(pstart)
    art3d.pathpatch_2d_to_3d(pstart, z=min_height, zdir="z")

    pfinish = Circle(finish, 0.5, ec=pec, fc=pfc)
    ax.add_patch(pfinish)
    art3d.pathpatch_2d_to_3d(pfinish, z=max_height, zdir="z")

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


def part_one(lines: List[str]):
    print('Part One')

    mountain = []
    start = None
    finish = None
    for ridx, line in enumerate(lines):
        row = []
        for cidx, c in enumerate(line):
            if c == 'S':
                row.append(ord('a') - SHIFT)
                start = (cidx, ridx)
            elif c == 'E':
                row.append(ord('z') - SHIFT)
                finish = (cidx, ridx)
            else:
                row.append(ord(c) - SHIFT)
        
        mountain.append(row)

    plot_mountain(mountain, start, finish)


def part_two(lines: List[str]):
    print('Part Two')


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
