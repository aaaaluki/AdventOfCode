#!/usr/bin/env python
import sys
import utils
from typing import List


def parts(lines:List[str]):
    for l in lines:
        print('{}{}{}'.format('\033[1m' + '\033[95m', l, '\033[0m'))
        stream = utils.Stream(l)
        stream.parse()
        print()

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
