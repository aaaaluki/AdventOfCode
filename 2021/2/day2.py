#!/usr/bin/env python
import sys

def part_one(lines):
    pos = [0, 0]    # horizontal, depth

    for i in range(len(lines)):
        commands = lines[i].split(' ')
        oper = commands[0]
        dist = int(commands[1])

        if oper == 'forward':
            pos[0] += dist
        elif oper == 'down':
            pos[1] += dist
        elif oper == 'up':
            pos[1] -= dist
        
    print("Part One")
    print("\tFinal position {}".format(pos))
    print("\tResult = {}".format(pos[0]*pos[1]))

    return

def part_two(lines):
    pos = [0, 0]    # horizontal, depth
    aim = 0

    for i in range(len(lines)):
        commands = lines[i].split(' ')
        oper = commands[0]
        dist = int(commands[1])

        if oper == 'forward':
            pos[0] += dist
            pos[1] += aim*dist
        elif oper == 'down':
            aim += dist
        elif oper == 'up':
            aim -= dist
        
    print("Part Two")
    print("\tFinal position: {}".format(pos))
    print("\tAim = {}".format(aim))
    print("\tResult = {}".format(pos[0]*pos[1]))


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