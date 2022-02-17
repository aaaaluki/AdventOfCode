#!/usr/bin/env python
from board import Board
import sys

def part_one(lines):
    print('Part One')
    N = 5   # Size of the boards

    # Get the drawn numbers
    drawn_numbers = [int(i) for i in lines[0].split(',')]
    
    # Init boards
    Board.next_idx = 0
    boards = []
    i = 2
    while i < len(lines):
        boards.append(Board(lines[i:i+5], N))
        i += N+1

    # Loop the drawn numbers until the winning board is found
    bingo = False
    last_drawn = drawn_numbers[0]
    for n in drawn_numbers:
        if bingo:
            break

        last_drawn = n

        for i in range(len(boards)):
            if boards[i].check_number(n):
                bingo = True
                print('BINGO!!!')
                break
    
    # Display the winning board and result
    b = boards[i]
    score = b.calculate_score()
    print('The winning board is number {}:'.format(b.m_idx))
    print(b)
    print('Final score = {}*{} = {}'.format(score, last_drawn, score*last_drawn))

    return

def part_two(lines):
    print('Part Two')
    N = 5   # Size of the boards

    # Get the drawn numbers
    drawn_numbers = [int(i) for i in lines[0].split(',')]
    
    # Init boards
    Board.next_idx = 0
    boards = []
    i = 2
    while i < len(lines):
        boards.append(Board(lines[i:i+5], N))
        i += N+1

    # Loop the drawn numbers until the losing board is found
    bingo = False
    last_drawn = drawn_numbers[0]
    for n in drawn_numbers:
        if bingo:
            break

        last_drawn = n

        # Init an empty array of board indices to remove
        to_remove = []
        for i in range(len(boards)):
            if boards[i].check_number(n):
                # If the board has made bingo added to remove
                to_remove.append(i)

                # When all the boards have made bingo we've found the last one
                if len(boards) == len(to_remove):
                    bingo = True

                    # Remove the losing board from removal
                    to_remove.pop()

                    print('Last BINGO!!!')
                    break
        
        # Remove the finished boards
        for i in reversed(to_remove):
            # Doing it in reverse, this way we won't get an: 
            #   "IndexError: list index out of range"
            boards.pop(i)
    
    # Display the losing board and result
    b = boards[0]
    score = b.calculate_score()
    print('The losing board is number {}:'.format(b.m_idx))
    print(b)
    print('Final score = {}*{} = {}'.format(score, last_drawn, score*last_drawn))

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