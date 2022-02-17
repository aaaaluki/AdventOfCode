#!/usr/bin/env python
from line import Line
from PIL import Image
import numpy as np
import sys

def part_one(lines):
    print('Part One')

    vents = []
    for l in lines:
        vents.append(Line(l))

    print('Canvas size: {}x{}'.format(Line.max_x + 1, Line.max_y + 1))
    canvas = np.zeros((Line.max_y + 1, Line.max_x + 1), dtype=np.int16)

    for v in vents:
        v.draw(canvas, diagonals=False)

    idx = np.where(canvas >= 2)
    print(canvas)
    save_image(canvas, filename + '1.png')

    print('Result = {}'.format(idx[0].size))
    
    return

def part_two(lines):
    print('Part Two')

    vents: list[Line] = []
    for l in lines:
        vents.append(Line(l))

    print('Canvas size: {}x{}'.format(Line.max_x + 1, Line.max_y + 1))
    canvas = np.zeros((Line.max_y + 1, Line.max_x + 1), dtype=np.int16)

    for v in vents:
        v.draw(canvas, diagonals=True)
        

    idx = np.where(canvas >= 2)
    print(canvas)
    save_image(canvas, filename + '2.png')

    print('Result = {}'.format(idx[0].size))
    
    return

def save_image(canvas, filename):
    # Normalize canvas 0-255 range
    canvas = np.floor((255 * canvas) / np.amax(canvas))

    # L for Luminance (Black & White)
    img = Image.fromarray(canvas, 'L')
    img.save(filename)

def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    global filename
    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        part_one(lines)
        part_two(lines)


if __name__ == '__main__':
    main(sys.argv)