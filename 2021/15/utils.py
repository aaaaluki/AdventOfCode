
from typing import Deque, Dict, List, Tuple
from collections import deque
from heapq import heappop, heappush
import numpy as np

infinity = float('inf')

def dijkstra(graph:List[List[int]], source:int, target:int) -> Deque[int]:
    # https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Pseudocode

    dist = {}
    prev = {}
    q = deque()

    for j in range(len(graph)):
        for i in range(len(graph[0])):
            dist[index(graph, (i, j))] = infinity
            prev[index(graph, (i, j))] = None
            q.append(index(graph, (i, j)))

    dist[source] = 0

    start_len = len(q)
    while len(q) != 0:
        u = min_dist(q, dist)
        q.remove(u)

        if u == target:
            break

        n = get_neighbors(graph, u)
        for v in n:
            if v in q:
                idx = inv_index(graph, v)
                alt = dist[u] + graph[idx[1]][idx[0]]

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    
    # Backtrace path
    stack = deque()
    u = target
    while u != None:
        stack.appendleft(u)
        u = prev[u]
    
    return stack


def a_star(graph:List[List[int]], source:int, target:int) -> Deque[int]:
    # https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
    
    open_set = {source}
    g_score = {}
    came_from = {}
    f_score = {}

    # Stay on the diagonal
    heuristic = lambda p: abs(p[0] - p[1])

    for j in range(len(graph)):
        for i in range(len(graph[0])):
            g_score[index(graph, (i, j))] = infinity
            g_score[index(graph, (i, j))] = infinity

    g_score[source] = 0
    f_score[source] = heuristic(inv_index(graph, source))

    heap = [(f_score[source], source)]

    while open_set:
        _, current = heappop(heap)
        if current == target:
            break
        
        for n in get_neighbors(graph, current):
            idx = inv_index(graph, n)
            tentative_g_score = g_score[current] + graph[idx[1]][idx[0]]
            if tentative_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = tentative_g_score + heuristic(inv_index(graph, n))
                if n not in open_set:
                    heappush(heap, (f_score[n], n))

    # Backtrace path
    stack = deque()
    u = target
    while u != 0:
        stack.appendleft(u)
        u = came_from[u]
    stack.appendleft(u)
    
    return stack

def min_dist(q, dist:Dict[int, int]) -> int:

    vertex = q[0]
    m = dist[q[0]]
    for v in q:
        if dist[v] < m:
            m = dist[v]
            vertex = v

    return vertex


def index(graph:List[List[int]], idx:Tuple[int, int]) -> int:
    return idx[1]*len(graph) + idx[0]


def inv_index(graph:List[List[int]], idx:int) -> Tuple[int, int]:
    return (idx % len(graph), idx // len(graph))


def get_neighbors(graph:List[List[int]], idx:int, digaonals:bool=False) -> List[int]:

    rows = len(graph)
    cols = len(graph[0])

    i = idx % rows
    j = idx // rows

    pos = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

    n = []
    for p in pos:
        if not (p[0] < 0 or p[1] < 0 or p[0] >= cols or p[1] >= rows):
            n.append(index(graph, p))

    return n


def calculate_risk(graph:List[List[int]], path:Deque[int]) -> int:
    risk = 0

    for i in range(1, len(path)):
        idx = inv_index(graph, path[i])
        risk += graph[idx[1]][idx[0]]
    
    return risk


def print_path(graph:List[List[int]], path:Deque[int]) -> None:

    for j in range(len(graph)):
        for i in range(len(graph[0])):
            if index(graph, (i, j)) in path:
                print('\u2588', end='')
            else:
                print('·', end='')
        
        print()


def expand(cell, x_expand:int, y_expand:int):
    result = cell - 1
    
    for i in range(x_expand - 1):
        G = (cell + i)
        result = np.hstack((result, G))
    
    row = result
    for j in range(1, y_expand):
        G = (row + j)
        result = np.vstack((result, G))
    
    return result % 9 + 1

