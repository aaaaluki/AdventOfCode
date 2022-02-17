
from typing import Counter


def find_local_minima(mat):
    rows = len(mat)
    cols = len(mat[0])

    minima = []
    for i in range(rows):
        for j in range(cols):
            if is_local_minima(mat, i , j):
                minima.append((i, j))
    
    return minima


def is_local_minima(mat, i, j):
    rows = len(mat)
    cols = len(mat[0])

    pos = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    for p in pos:
        k = p[0]
        l = p[1]
        if not (k < 0 or l < 0 or k == rows or l == cols):
            if mat[i][j] >= mat[k][l]:
                return False

    
    return True


def flood_fill(mat, node):
    # The algorithm is from the Wikipedia article: https://en.wikipedia.org/wiki/Flood_fill
    # The idea of using a flood-fill algorithm is taken from the
    # r/adventofcode subreddit

    rows = len(mat)
    cols = len(mat[0])

    count = 0

    # Set the empty queue and add node to the end of queue
    queue = [node]
    # While queue is not empty
    while len(queue) != 0:
        # Set n equal to the first element of queue
        n = queue[0]
        # Remove n from the queue
        queue = queue[1::]

        if n[0] < 0 or n[1] < 0 or n[0] == rows or n[1] == cols:
            # If n is not inside continue
            continue

        # If n is not set set it
        if mat[n[0]][n[1]] == 0:
            mat[n[0]][n[1]] = 1

            # Add W, E, N and S nodes to the end of Q
            queue.append((n[0], n[1] - 1))
            queue.append((n[0], n[1] + 1))
            queue.append((n[0] - 1, n[1]))
            queue.append((n[0] + 1, n[1]))

            count += 1

    return count