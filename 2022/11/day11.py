#!/usr/bin/python3
import sys
from math import floor
from typing import List


ROUNDS_P1 = 20
ROUNDS_P2 = 10000


def get_operations(test_file: bool):
    if test_file:
        operations = [None for _ in range(4)]
        operations[0] = lambda x: x * 19
        operations[1] = lambda x: x + 6
        operations[2] = lambda x: x * x
        operations[3] = lambda x: x + 3
    else:
        operations = [None for _ in range(8)]
        operations[0] = lambda x: x * 2
        operations[1] = lambda x: x + 3
        operations[2] = lambda x: x + 6
        operations[3] = lambda x: x + 5
        operations[4] = lambda x: x + 8
        operations[5] = lambda x: x * 5
        operations[6] = lambda x: x * x
        operations[7] = lambda x: x + 4

    return operations


def part_one(lines: List[str], test: bool):
    print('Part One')

    items = []
    operations = []
    test_value = []
    test_true = []
    test_false = []
    inspections = []

    gcd = 1

    monkeys_data = lines.split('\n\n')
    for monkey_data in monkeys_data:
        args = [l.strip() for l in monkey_data.split('\n')]
        monkey = {'items': [],
                  'operation': '', # Hard code it ;)
                  'test': 0,
                  'test_true': 0,
                  'test_false': 0}

        items.append([int(it) for it in args[1][16::].split(',')])
        test_value.append(int(args[3].split(' ')[-1]))
        test_true.append(int(args[4].split(' ')[-1]))
        test_false.append(int(args[5].split(' ')[-1]))
        inspections.append(0)

        gcd *= test_value[-1]

    operations = get_operations(test)

    for round_idx in range(1, ROUNDS_P1 + 1):
        for idx in range(len(items)):
            for item in items[idx]:
                worry = floor(operations[idx](item) / 3) % gcd
                inspections[idx] += 1

                if worry % test_value[idx] == 0:
                    items[test_true[idx]].append(worry)
                else:
                    items[test_false[idx]].append(worry)

            items[idx] = []

    print('# Inspections')
    for idx, inspec in enumerate(inspections):
        print(f'Monkey {idx}: {inspec}')

    print(f'result: {sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1]}')


def part_two(lines: List[str], test: bool):
    print('Part Two')

    items = []
    operations = []
    test_value = []
    test_true = []
    test_false = []
    inspections = []

    gcd = 1

    monkeys_data = lines.split('\n\n')
    for monkey_data in monkeys_data:
        args = [l.strip() for l in monkey_data.split('\n')]
        monkey = {'items': [],
                  'operation': '', # Hard code it ;)
                  'test': 0,
                  'test_true': 0,
                  'test_false': 0}

        items.append([int(it) for it in args[1][16::].split(',')])
        test_value.append(int(args[3].split(' ')[-1]))
        test_true.append(int(args[4].split(' ')[-1]))
        test_false.append(int(args[5].split(' ')[-1]))
        inspections.append(0)

        gcd *= test_value[-1]

    operations = get_operations(test)

    for round_idx in range(1, ROUNDS_P2 + 1):
        for idx in range(len(items)):
            for item in items[idx]:
                worry = floor(operations[idx](item)) % gcd
                inspections[idx] += 1

                if worry % test_value[idx] == 0:
                    items[test_true[idx]].append(worry)
                else:
                    items[test_false[idx]].append(worry)

            items[idx] = []

    print('# Inspections')
    for idx, inspec in enumerate(inspections):
        print(f'Monkey {idx}: {inspec}')

    print(f'result: {sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1]}')


def main(args):
    if len(args) < 2:
        print('[ERROR] Enter a file name!')
        print(f'\tUsage: python {args[0]} <filename>')
        sys.exit(1)

    filename = args[1]
    with open(filename, 'r') as f:
        lines = f.read()

    test = filename == 'test'
    part_one(lines, test)
    part_two(lines, test)


if __name__ == '__main__':
    main(sys.argv)
