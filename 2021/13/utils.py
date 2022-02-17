
from typing import List, Tuple


def read_input(lines:List[str]) -> Tuple[List[List[int]], List[Tuple[str, int]]]:
    read_folds = False
    paper = [[0]]
    folds = []

    for l in lines:
        if l == '':
            read_folds = True
            continue

        if not read_folds:
            x, y = l.split(',')
            x = int(x)
            y = int(y)

            rows = len(paper)
            cols = len(paper[0])
            if y >= rows:
                for _ in range(y - rows + 1):
                    paper.append([0]*cols)
            
            if x >= cols:
                for row in paper:
                    row += [0]*(x - cols + 1)

            paper[y][x] = 1

        else:
            l = l.replace('fold along ', '')
            axis, pos = l.split('=')

            folds.append((axis, int(pos)))


    return (paper, folds)

def fold(paper:List[List[int]], fold:Tuple[str, int]) -> List[List[int]]:
    axis = fold[0]
    pos = fold[1]
    rows = len(paper)
    cols = len(paper[0])

    if axis == 'x':
        folded_paper = [r[:pos] for r in paper]

        for j in range(rows):
            for i in range(pos, cols):
                if paper[j][i] == 1:
                    #print('({},{}) -> ({},{})'.format(i, j, 2*pos - i, j))
                    folded_paper[j][2*pos - i] = 1

    else:
        folded_paper = paper[:pos]

        for j in range(pos, rows):
            for i in range(cols):
                if paper[j][i] == 1:
                    #print('({},{}) -> ({},{})'.format(i, j, i, 2*pos - j))
                    folded_paper[2*pos - j][i] = 1
        

    paper = folded_paper
    return paper


def print_paper(paper:List[List[int]]) -> None:
    for row in paper:
        for i in row:
            if i == 1:
                print('\u2588', end='')
            else:
                print(' ', end='')
        
        print()


def sum_matrix(mat:List[List[int]]) -> int:
    c = 0
    for r in mat:
        c += sum(r)
    
    return c
