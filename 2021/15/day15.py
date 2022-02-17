#!/usr/bin/env python
import sys
import utils
import numpy as np
from typing import List


def part_one(lines:List[str]):
    print('Part One')

    cave = []
    for r in lines:
        cave.append([int(c) for c in r])
        
    target = len(cave)*len(cave[0]) - 1

    path_astar = utils.a_star(cave, 0, target)
    #utils.print_path(cave, path_astar)
    risk = utils.calculate_risk(cave, path_astar)
    print('Result [AStar]    = {}'.format(risk))

    
    #path_dijkstra = utils.dijkstra(cave, 0, target)
    #utils.print_path(cave, path_dijkstra)
    #risk = utils.calculate_risk(cave, path_dijkstra)
    #print('Result [Dijkstra] = {}'.format(risk))
    
    return

def part_two(lines:List[str]):
    print('Part Two')

    cave = []
    for r in lines:
        cave.append([int(c) for c in r])

    cave = np.matrix(cave)
    cave = utils.expand(cave, 5, 5)
    cave = cave.tolist()
    target = len(cave)*len(cave[0]) - 1


    path_astar = utils.a_star(cave, 0, target)
    risk_astar = utils.calculate_risk(cave, path_astar)
    #print('Result [AStar]    = {}'.format(risk))
    #utils.print_path(cave, path)
    print('Result [AStar]    = {}'.format(risk_astar))

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
