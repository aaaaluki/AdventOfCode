#!/usr/bin/env python
import sys
import utils

def part_one(lines):
    print('Part One')

    paper, folds = utils.read_input(lines)
    
    paper = utils.fold(paper, folds[0])
    print('Result = {}'.format(utils.sum_matrix(paper)))

    return

def part_two(lines):
    print('Part Two')

    paper, folds = utils.read_input(lines)

    for f in folds:
        paper = utils.fold(paper, f)
    
    utils.print_paper(paper)

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