#!/usr/bin/env python
import sys

def part_one(lines):
    print('Part One')

    opening = '([{<'
    closing = ')]}>'
    points = [3, 57, 1197, 25137]

    syntax_error_score = 0
    for l in lines:

        queue = []

        for c in l:
            if c in opening:
                queue.append(c)
            else:
                idx_found = closing.index(c)
                idx_desired = opening.index(queue[-1])

                if opening[idx_desired] != opening[idx_found]:
                    # print("{} <- Expected '{}', but found '{}' instead.".format(l, closing[idx_desired], c))
                    syntax_error_score += points[idx_found]
                    break

                else:
                    queue = queue[:-1]
    
    print('Syntax Error Score: {}'.format(syntax_error_score))


    return

def part_two(lines):
    print('Part Two')

    opening = '([{<'
    closing = ')]}>'
    points = [1, 2, 3, 4]

    scores = []
    for l in lines:

        queue = []
        discard = False
        for c in l:
            if c in opening:
                queue.append(c)
            else:
                idx_found = closing.index(c)
                idx_desired = opening.index(queue[-1])

                if opening[idx_desired] != opening[idx_found]:
                    discard = True
                    break

                else:
                    queue = queue[:-1]
        
        # If the line had a syntax error continue with the next one
        if discard:
            continue

        # Complete the line
        score = 0
        for c in range(len(queue) - 1, -1, -1):
            idx = opening.index(queue[c])
            score = 5*score + points[idx]
        
        scores.append(score)
    

    # Calculate the middle index as the ceil function of len/2, since len
    # will always be odd the obtained result is the index
    scores.sort()
    idx = (len(scores) >> 1)
    print(scores)
    print(idx)

    print('Middle score: {}'.format(scores[idx]))


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