from collections import defaultdict


def get_connections(arr):
    connections = defaultdict(list)

    for pair in arr:
        a, b = pair.split('-')

        connections[a].append(b)
        connections[b].append(a)


    return connections


def traverse(connections, can_twice, a='start', seen={'start'}):
    if a == 'end': yield 1
    else:
        for b in connections[a]:
            if b.islower():
                if b not in seen:
                    yield from traverse(connections, can_twice, b, seen | {b})
                elif can_twice and b not in {'start', 'end'}:
                    yield from traverse(connections, False, b, seen)
            else:
                yield from traverse(connections, can_twice, b, seen)
