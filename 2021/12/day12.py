#!/usr/bin/env python
import sys
from typing import TypeGuard
import utils


def part_one(lines):
    print('Part One')

    connections = utils.get_connections(lines)
    pathNum = utils.traverse(connections, False)
    print("Result = {}".format(sum(pathNum)))

    return

def part_two(lines):
    print('Part Two')

    connections = utils.get_connections(lines)
    pathNum = utils.traverse(connections, True)
    print("Result = {}".format(sum(pathNum)))

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